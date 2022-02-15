# ///////////////////////////////////////////////////////////////
# BY: Mateusz Koniuszewski
#
#
# Application design is modified version of project made by:
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

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from L5XModifier_functions import L5XModifier as L5XMod
from datetime import datetime

# os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
# widgets = None
VERSION = "v1.2.2"

# GLOBAL_STATE = False
# GLOBAL_TITLE_BAR = True


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.L5XMod = L5XMod()

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.clipboard = QGuiApplication.clipboard()
        # global widgets
        self.widgets = self.ui

        self.widgets.version.setText(VERSION)

        # INITIALIZE PAGES FUNCTIONALITY
        self.tE = ExportTagToCSV(self.widgets, self.L5XMod)
        self.sC = StringConverter(self.widgets, self.L5XMod)

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "L5X Modifier"
        description = "L5X Modifier - Tag to CSV"
        # APPLY TEXTS
        self.setWindowTitle(title)
        self.widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        self.widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # LEFT MENUS BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        self.widgets.btn_home.clicked.connect(self.buttonClick)
        self.widgets.btn_str_conv.clicked.connect(self.buttonClick)
        self.widgets.btn_exit.clicked.connect(self.closeEvent)
        self.widgets.btn_save.clicked.connect(self.save_file)

        # EXTRA RIGHT BOX
        # ///////////////////////////////////////////////////////////////
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        self.widgets.settingsTopBtn.clicked.connect(openCloseRightBox)
        # EXPORT ENCODING WINDOW
        self.widgets.pushButton_RB_ExportEncoding.clicked.connect(self.RB_clicked)
        self.widgets.lineEdit_RB_ExpEnc_RadioButton_Custom.editingFinished.connect(self.RB_radioButtons_custom_check)

        # CLOSE APP BUTTON
        # ///////////////////////////////////////////////////////////////
        self.widgets.closeAppBtn.clicked.connect(self.closeEvent)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        # themeFile = "themes\py_dracula_light.qss"
        themeFile = r"themes\py_dracula_au.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_tagExport)
        self.widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(self.widgets.btn_home.styleSheet()))

    def closeEvent(self, event):
        if isinstance(event, QCloseEvent):
            event.ignore()
        close_dialog = MyDialog(self)
        if close_dialog.exec():
            sys.exit()

    def display_error(self, message):
        self.widgets.errorLabel.setStyleSheet("color: red")
        self.widgets.errorLabel.setText(message)

    def display_warning(self, message):
        self.widgets.errorLabel.setStyleSheet("color: yellow")
        self.widgets.errorLabel.setText(message)

    def clear_error(self):
        self.widgets.errorLabel.clear()

    def save_file(self):
        self.clear_error()
        dialog = QFileDialog()
        dialog.setNameFilters(["RSLogix L5X files (*.L5X)"])
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setFileMode(QFileDialog.FileMode(0))
        if dialog.exec():
            file_name = dialog.selectedFiles()[0]
            self.L5XMod.save_file(file_name)

    def RB_radioButtons_get_encoder(self):
        radioButtons = {self.widgets.radioButton_RB_ExpEnc_UTF: "UTF-8"}
        for item in radioButtons:
            if item.isChecked():
                return radioButtons[item]
        if self.widgets.radioButton_RB_ExpEnc_system.isChecked():
            return None
        if self.widgets.radioButton_RB_ExpEnc_Custom.isChecked() and \
                self.widgets.lineEdit_RB_ExpEnc_RadioButton_Custom.text() != "":
            return self.widgets.lineEdit_RB_ExpEnc_RadioButton_Custom.text().lower()
        else:
            return None

    def RB_radioButtons_custom_check(self):
        if not self.L5XMod.check_custom_ecnoder(self.widgets.lineEdit_RB_ExpEnc_RadioButton_Custom.text()):
            self.widgets.lineEdit_RB_ExpEnc_RadioButton_Custom.clear()

    def RB_clicked(self):
        toolbox_buttons = {self.widgets.pushButton_RB_ExportEncoding: self.widgets.frame_RB_ExportEncoding}
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

    def choose_csv_file_load(self):
        self.clear_error()
        dialog = QFileDialog()
        dialog.setDefaultSuffix("cal")
        dialog.setNameFilters(["CSV (*.csv)", "All files (*.*)"])
        dialog.setWindowTitle('Select import CSV file')
        dialog.setFileMode(QFileDialog.FileMode(0))
        if dialog.exec():
            return dialog.selectedFiles()[0]

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
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_tagExport)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.widgets.titleRightInfo.setText('L5X Modifier - Tag to CSV')

        # SHOW WIDGETS PAGE
        if btnName == "btn_str_conv":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_strConverter)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.widgets.titleRightInfo.setText('L5X Modifier - String Converter')

        if btnName == "btn_save":
            self.save_file()

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
    # sys.stdout.close()
