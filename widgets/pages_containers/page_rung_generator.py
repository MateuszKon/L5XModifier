from main import MainWindow
from L5XModifier_functions import L5XModifier as L5XMod
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
import os
from PySide6.QtWidgets import QTreeWidgetItem


class RungGeneratorPage(MainWindow):

    def __init__(self, widgets, L5XMod_main):
        # COPIED FROM PARENT
        self.widgets = widgets
        # Main project object
        self.L5Xmain = L5XMod_main
        # Rungs Template
        self.L5Xrungs = L5XMod()
        # Faults Template
        self.L5Xfaults = L5XMod()

        # SUBCLASS PARAMETERS
        self.current_rung_file = ""
        self.appear_order_model = None
        self.alphabetical_order_model = None

        # SIGNALS AND SLOTS CONNECTIONS
        self.widgets.pushButton_rG_rungs_OpenFile.clicked.connect(self.rungs_openFile_button)
        self.widgets.lineEdit_rG_rungs_OpenFile.editingFinished.connect(self.rungs_file_changed)

    def rungs_openFile_button(self):
        dialog = QFileDialog()
        dialog.setNameFilters(["RSLogix exported rungs L5X files (*.L5X)"])
        if dialog.exec():
            self.widgets.lineEdit_rG_rungs_OpenFile.setText(dialog.selectedFiles()[0])
            self.rungs_file_changed()
        else:
            self.widgets.lineEdit_rG_rungs_OpenFile.setText(self.current_rung_file)

    def rungs_file_changed(self):
        self.clear_error()
        text = self.widgets.lineEdit_rG_rungs_OpenFile.text()
        ext = os.path.splitext(text)[-1].lower()
        if os.path.exists(text) and ext == ".l5x":
            self.current_rung_file = text
            self.L5Xrungs.open_file(text)
            self.populate_tree()
        else:
            self.rungs_openFile_button()

    def populate_tree(self):
        self.clear_error()
        header_data = [(0, Qt.Horizontal, "Tag"), (1, Qt.Horizontal, "DT"), (2, Qt.Horizontal, "Dsc"),
                       (3, Qt.Horizontal, "Val"), (4, Qt.Horizontal, "Scp")]

        # APPEAR OREDER MODEL GENERATION
        self.appear_order_model = QStandardItemModel(0, 5)
        for header in header_data:
            self.appear_order_model.setHeaderData(*header)
        self.L5Xrungs.generate_tree_appear_order(self.appear_order_model)
        self.appear_order_model.itemChanged.connect(self.appear_model_changed)

        # ALPHABETICLA OREDER MODEL GENERATION
        self.alphabetical_order_model = QStandardItemModel(0, 5)
        for header in header_data:
            self.alphabetical_order_model.setHeaderData(*header)
        self.L5Xrungs.generate_tree_alphabetical_order(self.alphabetical_order_model, self.appear_order_model)
        self.alphabetical_order_model.itemChanged.connect(self.alphabetical_model_changed)

        # CONNECTING APPEAR AND ALPHABETICAL MODELS TO TREE WIDGET
        self.widgets.treeView_trG.set_appear_order_model(self.appear_order_model)
        self.widgets.treeView_trG.set_alphabetical_order_model(self.alphabetical_order_model)

        # DISPLAYING MODEL
        self.widgets.treeView_trG.setModel(self.alphabetical_order_model)
        self.widgets.treeView_trG.expandAll()
        for i in range(4, -1, -1):
            self.widgets.treeView_trG.resizeColumnToContents(i)

    def appear_model_changed(self, item):
        item.update_tag_element()

    def alphabetical_model_changed(self, item):
        item.update_tag_element()
