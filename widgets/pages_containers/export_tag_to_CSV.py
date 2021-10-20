from main import MainWindow
import os
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QStandardItemModel
from PySide6.QtCore import Qt


class ExportTagToCSV(MainWindow):

    def __init__(self, widgets, L5XMod):
        # COPIED FROM PARENT
        self.widgets = widgets
        self.L5XMod = L5XMod

        # SUBCLASS PARAMETERS
        self.currentFile = ""

        # SIGNALS AND SLOTS CONNECTIONS
        self.widgets.pushButton_tE_OpenFile.clicked.connect(self.openFile_button)
        self.widgets.lineEdit_tE_OpenFile.editingFinished.connect(self.openFile_changed)
        self.widgets.comboBox_tE_ChooseScope.currentTextChanged.connect(self.chooseScope_changed)
        self.widgets.lineEdit_tE_Filter.textChanged.connect(self.ChooseTag_update_list)
        self.widgets.pushButton_tE_Filter.clicked.connect(widgets.lineEdit_tE_Filter.clear)
        self.widgets.listWidget_tE_ChooseTag.itemSelectionChanged.connect(self.tagTree_populate)
        self.widgets.checkBox_tE_PrintHeaders.stateChanged.connect(self.tagTree_populate)
        self.widgets.checkBox_tE_ConcatenatePath.stateChanged.connect(self.tagTree_populate)
        self.widgets.checkBox_tE_PrintHeaders.stateChanged.connect(self.check_checkboxes_state)
        self.widgets.checkBox_tE_ConcatenatePath.stateChanged.connect(self.check_checkboxes_state)
        self.widgets.radioButton_tE_Custom.clicked.connect(self.tagTree_populate)
        self.widgets.radioButton_tE_GFS.clicked.connect(self.tagTree_populate)
        self.widgets.radioButton_tE_PL.clicked.connect(self.tagTree_populate)
        self.widgets.radioButton_tE_RU.clicked.connect(self.tagTree_populate)
        self.widgets.radioButton_tE_UTF.clicked.connect(self.tagTree_populate)
        self.widgets.tE_RadioButton_group.toggled.connect(self.tagTree_populate)
        self.widgets.pushButton_tE_Expand.clicked.connect(widgets.treeView_tE_TagTree.expandAll)
        self.widgets.pushButton_tE_Collapse.clicked.connect(widgets.treeView_tE_TagTree.collapseAll)
        self.widgets.lineEdit_tE_RadioButton_Custom.editingFinished.connect(self.radioButtons_custom_check)
        self.widgets.pushButton_tE_Export.clicked.connect(self.export_CSV)
        self.widgets.pushButton_tE_Import.clicked.connect(self.import_CSV)

    def openFile_button(self):
        dialog = QFileDialog()
        dialog.setNameFilters(["RSLogix L5X files (*.L5X)"])
        if dialog.exec():
            self.widgets.lineEdit_tE_OpenFile.setText(dialog.selectedFiles()[0])
            self.openFile_changed()
        else:
            self.widgets.lineEdit_tE_OpenFile.setText(self.currentFile)

    def openFile_changed(self):
        self.clear_error()
        text = self.widgets.lineEdit_tE_OpenFile.text()
        ext = os.path.splitext(text)[-1].lower()
        if os.path.exists(text) and ext == ".l5x":
            self.currentFile = text
            self.L5XMod.open_file(text)
            self.chooseScope_populate()
        else:
            self.openFile_button()

    def chooseScope_populate(self):
        self.widgets.comboBox_tE_ChooseScope.clear()
        self.widgets.comboBox_tE_ChooseScope.addItems(self.L5XMod.get_scope())
        self.ChooseTag_update_list()

    def chooseScope_changed(self):
        self.clear_error()
        self.L5XMod.scope_changed(self.widgets.comboBox_tE_ChooseScope.currentText())
        self.ChooseTag_update_list()

    def ChooseTag_update_list(self):
        self.clear_error()
        self.widgets.listWidget_tE_ChooseTag.clear()
        filter_text = self.L5XMod.get_tag_list_filtered(self.widgets.lineEdit_tE_Filter.text())
        self.widgets.listWidget_tE_ChooseTag.addItems(filter_text)

    def tagTree_populate(self):
        self.clear_error()
        if self.widgets.listWidget_tE_ChooseTag.currentItem() is not None:
            top_most_model = QStandardItemModel(0, 3)
            top_most_model.setHeaderData(0, Qt.Horizontal, "Name")
            top_most_model.setHeaderData(1, Qt.Horizontal, "Data Type")
            top_most_model.setHeaderData(2, Qt.Horizontal, "Value")
            self.widgets.treeView_tE_TagTree.setModel(top_most_model)
            tag_name = self.widgets.listWidget_tE_ChooseTag.currentItem().text()
            scope = self.widgets.comboBox_tE_ChooseScope.currentText()
            encoder = self.radioButtons_get_encoder()
            print_headers = self.widgets.checkBox_tE_PrintHeaders.isChecked()
            concatenate = self.widgets.checkBox_tE_ConcatenatePath.isChecked()
            tag_tuple = self.L5XMod.get_tag_info_tuple(tag_name, scope, encoder=encoder)
            self.L5XMod.insert_into_tree(top_most_model, tag_tuple, print_headers, concatenate, encoder=encoder)
            self.widgets.treeView_tE_TagTree.expandAll()
            self.widgets.treeView_tE_TagTree.resizeColumnToContents(2)
            self.widgets.treeView_tE_TagTree.resizeColumnToContents(1)
            self.widgets.treeView_tE_TagTree.resizeColumnToContents(0)

    def radioButtons_get_encoder(self):
        radioButtons = {self.widgets.radioButton_tE_PL: "Windows-1250", self.widgets.radioButton_tE_GFS: "Windows-1252",
                        self.widgets.radioButton_tE_RU: "Windows-1251", self.widgets.radioButton_tE_UTF: "UTF-8"}
        for item in radioButtons:
            if item.isChecked():
                return radioButtons[item]
        if self.widgets.radioButton_tE_Custom.isChecked() and self.widgets.lineEdit_tE_RadioButton_Custom.text() != "":
            return self.widgets.lineEdit_tE_RadioButton_Custom.text().lower()
        else:
            return None

    def radioButtons_custom_check(self):
        if not self.L5XMod.check_custom_ecnoder(self.widgets.lineEdit_tE_RadioButton_Custom.text()):
            self.widgets.lineEdit_tE_RadioButton_Custom.clear()
        elif self.widgets.radioButton_tE_Custom.isChecked():
            self.tagTree_populate()

    def check_checkboxes_state(self):
        if not self.widgets.checkBox_tE_PrintHeaders.isChecked() and\
                not self.widgets.checkBox_tE_ConcatenatePath.isChecked():
            self.display_warning("Exporting tag without headers nor path concatenation will make impossible to import "
                                 "this tag")

    def export_CSV(self):
        self.clear_error()
        save_file = self.choose_csv_file_save()
        if save_file:
            output_encoder = self.RB_radioButtons_get_encoder()
            self.L5XMod.export_tag_to_csv(self.widgets.treeView_tE_TagTree, save_file, output_encoder)

    def import_CSV(self):
        self.clear_error()
        load_file = self.choose_csv_file_load()
        if load_file:
            file_encoder = self.RB_radioButtons_get_encoder()
            tag_encoder = self.radioButtons_get_encoder()
            scope = self.widgets.comboBox_tE_ChooseScope.currentText()
            self.L5XMod.import_tag_from_csv(load_file, scope=scope, file_encoding=file_encoder, encoding=tag_encoder)
            self.tagTree_populate()
