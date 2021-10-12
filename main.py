# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from L5XModifier_functions import L5XModifier as L5XMod
import warnings
from datetime import datetime

# os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
VERSION = "v1.2.0"

GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.L5XMod = L5XMod()

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.clipboard = QGuiApplication.clipboard()
        global widgets
        widgets = self.ui
        widgets.version.setText(VERSION)

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "L5X Modifier"
        description = "L5X Modifier - Tag to CSV"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_str_conv.clicked.connect(self.buttonClick)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        # themeFile = "themes\py_dracula_light.qss"
        themeFile = "themes\py_dracula_au.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.page_tagExport)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        # ///////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////
        # CUSTOM
        # ///////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////
        self.currentFile = ""
        self.tree = None
        widgets.pushButton_tE_OpenFile.clicked.connect(self.tE_openFile_button)
        widgets.lineEdit_tE_OpenFile.editingFinished.connect(self.tE_openFile_changed)
        widgets.comboBox_tE_ChooseScope.currentTextChanged.connect(self.tE_chooseScope_changed)
        widgets.lineEdit_tE_Filter.textChanged.connect(self.tE_ChooseTag_update_list)
        widgets.pushButton_tE_Filter.clicked.connect(widgets.lineEdit_tE_Filter.clear)
        widgets.listWidget_tE_ChooseTag.itemSelectionChanged.connect(self.tE_tagTree_populate)
        widgets.checkBox_tE_PrintHeaders.stateChanged.connect(self.tE_tagTree_populate)
        widgets.checkBox_tE_ConcatenatePath.stateChanged.connect(self.tE_tagTree_populate)
        widgets.checkBox_tE_PrintHeaders.stateChanged.connect(self.tE_check_checkboxes_state)
        widgets.checkBox_tE_ConcatenatePath.stateChanged.connect(self.tE_check_checkboxes_state)
        widgets.radioButton_tE_Custom.clicked.connect(self.tE_tagTree_populate)
        widgets.radioButton_tE_GFS.clicked.connect(self.tE_tagTree_populate)
        widgets.radioButton_tE_PL.clicked.connect(self.tE_tagTree_populate)
        widgets.radioButton_tE_RU.clicked.connect(self.tE_tagTree_populate)
        widgets.radioButton_tE_UTF.clicked.connect(self.tE_tagTree_populate)
        widgets.tE_RadioButton_group.toggled.connect(self.tE_tagTree_populate)
        widgets.pushButton_tE_Expand.clicked.connect(widgets.treeView_tE_TagTree.expandAll)
        widgets.pushButton_tE_Collapse.clicked.connect(widgets.treeView_tE_TagTree.collapseAll)
        widgets.lineEdit_tE_RadioButton_Custom.editingFinished.connect(self.tE_radioButtons_custom_check)
        widgets.pushButton_RB_ExportEncoding.clicked.connect(self.RB_clicked)
        widgets.lineEdit_RB_ExpEnc_RadioButton_Custom.editingFinished.connect(self.RB_radioButtons_custom_check)
        widgets.pushButton_tE_Export.clicked.connect(self.tE_export)
        widgets.pushButton_tE_Import.clicked.connect(self.tE_import)
        widgets.btn_exit.clicked.connect(self.closeEvent)
        widgets.btn_save.clicked.connect(self.save_file)
        widgets.closeAppBtn.clicked.connect(self.closeEvent)
        # page_strConverter
        widgets.lineEdit_tsC_RadioButton_Custom.editingFinished.connect(self.tsC_radioButtons_custom_check)
        widgets.radioButton_tsC_PL.clicked.connect(self.tsC_simpleText_translate)
        widgets.radioButton_tsC_GFS.clicked.connect(self.tsC_simpleText_translate)
        widgets.radioButton_tsC_RU.clicked.connect(self.tsC_simpleText_translate)
        widgets.radioButton_tsC_UTF.clicked.connect(self.tsC_simpleText_translate)
        widgets.textEdit_tsC_SimpleText.textChanged.connect(self.tsC_simpleText_translate)
        widgets.textEdit_tsC_RSLogixText.textChanged.connect(self.tsC_RSLText_edited)
        widgets.pushButton_tsC_CopyText.clicked.connect(self.tsC_CopyTest_clicked)
        widgets.pushButton_tsC_CopyRSL.clicked.connect(self.tsC_CopyRSL_clicked)
        widgets.pushButton_tsC_PasteText.clicked.connect(self.tsC_PasteText_clicked)
        widgets.pushButton_tsC_PasteRSL.clicked.connect(self.tsC_PasteRSL_clicked)

    def closeEvent(self, event):
        if isinstance(event, QCloseEvent):
            event.ignore()
        close_dialog = MyDialog(self)
        if close_dialog.exec():
            sys.exit()

    @staticmethod
    def display_error(message):
        widgets.errorLabel.setStyleSheet("color: red")
        widgets.errorLabel.setText(message)

    @staticmethod
    def display_warning(message):
        widgets.errorLabel.setStyleSheet("color: yellow")
        widgets.errorLabel.setText(message)

    @staticmethod
    def clear_error():
        widgets.errorLabel.clear()

    def save_file(self):
        self.clear_error()
        dialog = QFileDialog()
        dialog.setNameFilters(["RSLogix L5X files (*.L5X)"])
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setFileMode(QFileDialog.FileMode(0))
        if dialog.exec():
            file_name = dialog.selectedFiles()[0]
            self.L5XMod.save_file(file_name)


    def tE_openFile_button(self):
        dialog = QFileDialog()
        dialog.setNameFilters(["RSLogix L5X files (*.L5X)"])
        if dialog.exec():
            widgets.lineEdit_tE_OpenFile.setText(dialog.selectedFiles()[0])
            self.tE_openFile_changed()
        else:
            widgets.lineEdit_tE_OpenFile.setText(self.currentFile)

    def tE_openFile_changed(self):
        self.clear_error()
        text = widgets.lineEdit_tE_OpenFile.text()
        ext = os.path.splitext(text)[-1].lower()
        if os.path.exists(text) and ext == ".l5x":
            self.currentFile = text
            self.L5XMod.open_file(text)
            self.tE_chooseScope_populate()
        else:
            self.tE_openFile_button()

    def tE_chooseScope_populate(self):
        widgets.comboBox_tE_ChooseScope.clear()
        widgets.comboBox_tE_ChooseScope.addItems(self.L5XMod.get_scope())
        self.tE_ChooseTag_update_list()

    def tE_chooseScope_changed(self):
        self.clear_error()
        self.L5XMod.scope_changed(widgets.comboBox_tE_ChooseScope.currentText())
        self.tE_ChooseTag_update_list()

    def tE_ChooseTag_update_list(self):
        self.clear_error()
        widgets.listWidget_tE_ChooseTag.clear()
        filter_text = self.L5XMod.get_tag_list_filtered(widgets.lineEdit_tE_Filter.text())
        widgets.listWidget_tE_ChooseTag.addItems(filter_text)

    def tE_tagTree_populate(self):
        self.clear_error()
        if widgets.listWidget_tE_ChooseTag.currentItem() is not None:
            top_most_model = QStandardItemModel(0,3)
            top_most_model.setHeaderData(0, Qt.Horizontal, "Name")
            top_most_model.setHeaderData(1, Qt.Horizontal, "Data Type")
            top_most_model.setHeaderData(2, Qt.Horizontal, "Value")
            widgets.treeView_tE_TagTree.setModel(top_most_model)
            tag_name = widgets.listWidget_tE_ChooseTag.currentItem().text()
            scope = widgets.comboBox_tE_ChooseScope.currentText()
            encoder = self.tE_radioButtons_get_encoder()
            print_headers = widgets.checkBox_tE_PrintHeaders.isChecked()
            concatenate = widgets.checkBox_tE_ConcatenatePath.isChecked()
            tag_tuple = self.L5XMod.get_tag_info_tuple(tag_name, scope, encoder=encoder)
            self.L5XMod.insert_into_tree(top_most_model, tag_tuple, print_headers, concatenate, encoder=encoder)
            widgets.treeView_tE_TagTree.expandAll()
            widgets.treeView_tE_TagTree.resizeColumnToContents(2)
            widgets.treeView_tE_TagTree.resizeColumnToContents(1)
            widgets.treeView_tE_TagTree.resizeColumnToContents(0)

    def tE_radioButtons_get_encoder(self):
        radioButtons = {widgets.radioButton_tE_PL: "Windows-1250", widgets.radioButton_tE_GFS: "Windows-1252",
                        widgets.radioButton_tE_RU: "Windows-1251", widgets.radioButton_tE_UTF: "UTF-8"}
        for item in radioButtons:
            # selected_radio = self.ui.findChild(QRadioButton, item)
            if item.isChecked():
                return radioButtons[item]
        if widgets.radioButton_tE_Custom.isChecked() and widgets.lineEdit_tE_RadioButton_Custom.text() != "":
            return widgets.lineEdit_tE_RadioButton_Custom.text().lower()
        else:
            return None

    def tE_radioButtons_custom_check(self):
        if not self.L5XMod.check_custom_ecnoder(widgets.lineEdit_tE_RadioButton_Custom.text()):
            widgets.lineEdit_tE_RadioButton_Custom.clear()
        elif widgets.radioButton_tE_Custom.isChecked():
            self.tE_tagTree_populate()

    def tE_check_checkboxes_state(self):
        if not widgets.checkBox_tE_PrintHeaders.isChecked() and\
                not widgets.checkBox_tE_ConcatenatePath.isChecked():
            self.display_warning("Exporting tag without headers nor path concatenation will make impossible to import "
                                 "this tag")

    def RB_radioButtons_get_encoder(self):
        radioButtons = {widgets.radioButton_RB_ExpEnc_UTF: "UTF-8"}
        for item in radioButtons:
            if item.isChecked():
                return radioButtons[item]
        if widgets.radioButton_RB_ExpEnc_system.isChecked():
            return None
        if widgets.radioButton_RB_ExpEnc_Custom.isChecked() and \
                widgets.lineEdit_RB_ExpEnc_RadioButton_Custom.text() != "":
            return widgets.lineEdit_RB_ExpEnc_RadioButton_Custom.text().lower()
        else:
            return None

    def RB_radioButtons_custom_check(self):
        if not self.L5XMod.check_custom_ecnoder(widgets.lineEdit_RB_ExpEnc_RadioButton_Custom.text()):
            widgets.lineEdit_RB_ExpEnc_RadioButton_Custom.clear()

    def RB_clicked(self):
        toolbox_buttons = {widgets.pushButton_RB_ExportEncoding: widgets.frame_RB_ExportEncoding}
        btn = self.sender()
        UIFunctions.open_right_toolbox(self, toolbox_buttons[btn])

    def choose_csv_file_save(self):
        self.clear_error()
        dialog = QFileDialog()
        dialog.setDefaultSuffix("cal")
        dialog.setNameFilters(["CSV (*.csv)", "All files (*.*)"])
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setWindowTitle('Select save CSV file')
        dialog.setFileMode(QFileDialog.FileMode(0))
        if dialog.exec():
            return dialog.selectedFiles()[0]

    def tE_export(self):
        self.clear_error()
        save_file = self.choose_csv_file_save()
        if save_file:
            output_encoder = self.RB_radioButtons_get_encoder()
            self.L5XMod.export_tag_to_csv(widgets.treeView_tE_TagTree, save_file, output_encoder)

    def choose_csv_file_load(self):
        self.clear_error()
        dialog = QFileDialog()
        dialog.setDefaultSuffix("cal")
        dialog.setNameFilters(["CSV (*.csv)", "All files (*.*)"])
        dialog.setWindowTitle('Select import CSV file')
        dialog.setFileMode(QFileDialog.FileMode(0))
        if dialog.exec():
            return dialog.selectedFiles()[0]

    def tE_import(self):
        self.clear_error()
        load_file = self.choose_csv_file_load()
        if load_file:
            file_encoder = self.RB_radioButtons_get_encoder()
            tag_encoder = self.tE_radioButtons_get_encoder()
            scope = widgets.comboBox_tE_ChooseScope.currentText()
            self.L5XMod.import_tag_from_csv(load_file, scope=scope, file_encoding=file_encoder, encoding=tag_encoder)
            self.tE_tagTree_populate()

    def tsC_radioButtons_get_encoder(self):
        radioButtons = {widgets.radioButton_tsC_PL: "Windows-1250", widgets.radioButton_tsC_GFS: "Windows-1252",
                        widgets.radioButton_tsC_RU: "Windows-1251", widgets.radioButton_tsC_UTF: "UTF-8"}
        for item in radioButtons:
            if item.isChecked():
                return radioButtons[item]
        if widgets.radioButton_tsC_Custom.isChecked() and widgets.lineEdit_tsC_RadioButton_Custom.text() != "":
            return widgets.lineEdit_tsC_RadioButton_Custom.text().lower()
        else:
            return None

    def tsC_radioButtons_custom_check(self):
        if not self.L5XMod.check_custom_ecnoder(widgets.lineEdit_tsC_RadioButton_Custom.text()):
            widgets.lineEdit_tsC_RadioButton_Custom.clear()
        elif widgets.radioButton_tsC_Custom.isChecked():
            self.tsC_simpleText_translate()

    def tsC_simpleText_translate(self):
        self.clear_error()
        string = widgets.textEdit_tsC_SimpleText.toPlainText()
        encoder = self.tsC_radioButtons_get_encoder()
        widgets.textEdit_tsC_RSLogixText.blockSignals(True)
        with warnings.catch_warnings(record=True) as w:
            widgets.textEdit_tsC_RSLogixText.setPlainText(self.L5XMod.encode_string(string, encoder))
            if w:
                print("Warning: " + str(w[-1]))
                self.display_error(str(w[-1].message))
        widgets.textEdit_tsC_RSLogixText.blockSignals(False)

    def tsC_RSLText_edited(self):
        self.clear_error()
        string = widgets.textEdit_tsC_RSLogixText.toPlainText()
        encoder = self.tsC_radioButtons_get_encoder()
        widgets.textEdit_tsC_SimpleText.blockSignals(True)
        widgets.textEdit_tsC_SimpleText.setPlainText(self.L5XMod.decode_string(string, encoder))
        widgets.textEdit_tsC_SimpleText.blockSignals(False)


    def tsC_CopyTest_clicked(self):
        self.clear_error()
        self.clipboard.setText(widgets.textEdit_tsC_SimpleText.toPlainText())

    def tsC_CopyRSL_clicked(self):
        self.clear_error()
        self.clipboard.setText(widgets.textEdit_tsC_RSLogixText.toPlainText())

    def tsC_PasteText_clicked(self):
        self.clear_error()
        widgets.textEdit_tsC_SimpleText.setPlainText(self.clipboard.text())

    def tsC_PasteRSL_clicked(self):
        self.clear_error()
        widgets.textEdit_tsC_RSLogixText.setPlainText(self.clipboard.text())


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        self.clear_error()

        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.page_tagExport)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            widgets.titleRightInfo.setText('L5X Modifier - Tag to CSV')

        # SHOW WIDGETS PAGE
        if btnName == "btn_str_conv":
            widgets.stackedWidget.setCurrentWidget(widgets.page_strConverter)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            widgets.titleRightInfo.setText('L5X Modifier - String Converter')

        if btnName == "btn_save":
            self.save_file()

        # # SHOW NEW PAGE
        # if btnName == "btn_new":
        #     widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
        #     UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
        #     btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos


class UIFunctions(MainWindow):
    # MAXIMIZE/RESTORE
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            # self.ui.MainWindow.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            # self.ui.MainWindow.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return GLOBAL_STATE

    # SET STATUS
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # TOGGLE LEFT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleLeftBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraLeftBox.width()
            widthRightBox = self.ui.extraRightBox.width()
            maxExtend = Settings.LEFT_BOX_WIDTH
            color = Settings.BTN_LEFT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.toggleLeftBox.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.toggleLeftBox.setStyleSheet(style + color)
                if widthRightBox != 0:
                    style = self.ui.settingsTopBtn.styleSheet()
                    self.ui.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))

        UIFunctions.start_box_animation(self, width, widthRightBox, "left")

    # TOGGLE RIGHT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleRightBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraRightBox.width()
            widthLeftBox = self.ui.extraLeftBox.width()
            maxExtend = Settings.RIGHT_BOX_WIDTH
            color = Settings.BTN_RIGHT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.settingsTopBtn.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.settingsTopBtn.setStyleSheet(style + color)
                if widthLeftBox != 0:
                    style = self.ui.toggleLeftBox.styleSheet()
                    self.ui.toggleLeftBox.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

            UIFunctions.start_box_animation(self, widthLeftBox, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0

            # ANIMATION LEFT BOX
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # IMPORT THEMES FILES QSS/CSS
    # ///////////////////////////////////////////////////////////////
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            # STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    p = event.globalPosition()
                    globalPos = p.toPoint()
                    self.move(self.pos() + globalPos - self.dragPos)
                    self.dragPos = globalPos
                    event.accept()

            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

    def resize_grips(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS

    def open_right_toolbox(self, open_widget: QFrame):
        height = open_widget.height()
        maxheight = 500
        standard = 0
        if height > 0:
            new_height = standard
        else:
            new_height = maxheight
        UIFunctions.right_toolbox_animation(self, open_widget, new_height, height)

    def right_toolbox_animation(self, open_widget: QFrame, new_height, old_height):
        self.right_toolbox = QPropertyAnimation(open_widget, b"maximumHeight")
        self.right_toolbox.setDuration(Settings.TIME_ANIMATION)
        self.right_toolbox.setStartValue(old_height)
        self.right_toolbox.setEndValue(new_height)
        self.right_toolbox.setEasingCurve(QEasingCurve.InOutQuart)
        self.right_toolbox.start()


# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class AppFunctions(MainWindow):
    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(62, 73, 230, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """
# rgba(255, 121, 198, 255)

        # SET MANUAL STYLES
        self.ui.scrollArea_tE.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.scrollArea_tsC.setStyleSheet("QPushButton {background-color: rgb(52, 59, 72);} "
                                             "QPlainTextEdit {font: 16pt;}")
        # "QTextEdit {background-color: red; color: rgb(221, 221, 221); font: 16pt;}")


if __name__ == "__main__":
    # LOG FILE MANAGEMENT
    directory = os.getcwd()
    if not os.path.isdir(directory + "\\log"):
        os.mkdir(directory + "\\log")
    log_file_path = directory + '\\log\\log_{}.txt'.format(datetime.now().strftime("%Y%m%d_%H%M%S"))
    sys.stdout = MyLogger(sys.stdout, log_file_path)

    # GUI START
    app = QApplication(sys.argv)
    app_icon = QIcon()
    app_icon.addFile('ico/Au_16.png', QSize(16, 16))
    app_icon.addFile('ico/Au_32.png', QSize(32, 32))
    app_icon.addFile('ico/Au_48.png', QSize(48, 48))
    app_icon.addFile('ico/Au_128.png', QSize(128, 128))
    app.setWindowIcon(app_icon)
    window = MainWindow()
    sys.exit(app.exec())

    # CLOSE LOG FILE
    sys.stdout.close()
