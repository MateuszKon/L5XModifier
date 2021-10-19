# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainBarwxy.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1052, 541)
        MainWindow.setMinimumSize(QSize(470, 280))
        MainWindow.setAutoFillBackground(True)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	backg"
                        "round-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/ico/ico/Au_48.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(85, 170, 255); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);"
                        "\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249"
                        ");\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px sol"
                        "id rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; bo"
                        "rder-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 25"
                        "5);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, "
                        "37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255"
                        ", 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:"
                        ":sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-or"
                        "igin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-imag"
                        "e: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-posit"
                        "ion: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px"
                        ";\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	"
                        "\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// \n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"	font-style: normal;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#textEdit_tsC_SimpleText {\n"
"	color: rgb(221, 221, 221);\n"
"	font: 16pt \"Segoe UI\";\n"
"}\n"
""
                        "\n"
"#textEdit_tsC_RSLogixText {\n"
"	color: rgb(221, 221, 221);\n"
"	font: 16pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(4, 2, 48, 48))
        self.topLogo.setMinimumSize(QSize(48, 48))
        self.topLogo.setMaximumSize(QSize(48, 48))
        self.topLogo.setStyleSheet(u"")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-align-center.png);")
        self.btn_home.setIconSize(QSize(16, 16))

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_str_conv = QPushButton(self.topMenu)
        self.btn_str_conv.setObjectName(u"btn_str_conv")
        sizePolicy.setHeightForWidth(self.btn_str_conv.sizePolicy().hasHeightForWidth())
        self.btn_str_conv.setSizePolicy(sizePolicy)
        self.btn_str_conv.setMinimumSize(QSize(0, 45))
        self.btn_str_conv.setFont(font)
        self.btn_str_conv.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_str_conv.setLayoutDirection(Qt.LeftToRight)
        self.btn_str_conv.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-paragraph.png);")

        self.verticalLayout_8.addWidget(self.btn_str_conv)

        self.btn_rungGenerator = QPushButton(self.topMenu)
        self.btn_rungGenerator.setObjectName(u"btn_rungGenerator")
        sizePolicy.setHeightForWidth(self.btn_rungGenerator.sizePolicy().hasHeightForWidth())
        self.btn_rungGenerator.setSizePolicy(sizePolicy)
        self.btn_rungGenerator.setMinimumSize(QSize(0, 45))
        self.btn_rungGenerator.setFont(font)
        self.btn_rungGenerator.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_rungGenerator.setLayoutDirection(Qt.LeftToRight)
        self.btn_rungGenerator.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-view-quilt.png);")

        self.verticalLayout_8.addWidget(self.btn_rungGenerator)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png);")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setEnabled(True)
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_tagExport = QWidget()
        self.page_tagExport.setObjectName(u"page_tagExport")
        self.page_tagExport.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.page_tagExport)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.scrollArea_tE = QScrollArea(self.page_tagExport)
        self.scrollArea_tE.setObjectName(u"scrollArea_tE")
        self.scrollArea_tE.setWidgetResizable(True)
        self.scrollAreaWidgetContents_tE = QWidget()
        self.scrollAreaWidgetContents_tE.setObjectName(u"scrollAreaWidgetContents_tE")
        self.scrollAreaWidgetContents_tE.setGeometry(QRect(0, 0, 681, 294))
        self.horizontalLayout_7 = QHBoxLayout(self.scrollAreaWidgetContents_tE)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tE_LeftColumn = QVBoxLayout()
        self.tE_LeftColumn.setObjectName(u"tE_LeftColumn")
        self.tE_OpenFile = QGridLayout()
        self.tE_OpenFile.setObjectName(u"tE_OpenFile")
        self.tE_OpenFile.setVerticalSpacing(0)
        self.pushButton_tE_OpenFile = QPushButton(self.scrollAreaWidgetContents_tE)
        self.pushButton_tE_OpenFile.setObjectName(u"pushButton_tE_OpenFile")
        self.pushButton_tE_OpenFile.setMinimumSize(QSize(100, 30))
        self.pushButton_tE_OpenFile.setFont(font)
        self.pushButton_tE_OpenFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_tE_OpenFile.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_tE_OpenFile.setIcon(icon4)

        self.tE_OpenFile.addWidget(self.pushButton_tE_OpenFile, 1, 1, 1, 1)

        self.labelBox_tE_OpenFile = QLabel(self.scrollAreaWidgetContents_tE)
        self.labelBox_tE_OpenFile.setObjectName(u"labelBox_tE_OpenFile")
        self.labelBox_tE_OpenFile.setFont(font)
        self.labelBox_tE_OpenFile.setStyleSheet(u"")

        self.tE_OpenFile.addWidget(self.labelBox_tE_OpenFile, 0, 0, 1, 2)

        self.lineEdit_tE_OpenFile = QLineEdit(self.scrollAreaWidgetContents_tE)
        self.lineEdit_tE_OpenFile.setObjectName(u"lineEdit_tE_OpenFile")
        self.lineEdit_tE_OpenFile.setMinimumSize(QSize(0, 30))
        self.lineEdit_tE_OpenFile.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.tE_OpenFile.addWidget(self.lineEdit_tE_OpenFile, 1, 0, 1, 1)


        self.tE_LeftColumn.addLayout(self.tE_OpenFile)

        self.tE_ChooseScope = QVBoxLayout()
        self.tE_ChooseScope.setSpacing(0)
        self.tE_ChooseScope.setObjectName(u"tE_ChooseScope")
        self.labelBox_tE_ChooseScope = QLabel(self.scrollAreaWidgetContents_tE)
        self.labelBox_tE_ChooseScope.setObjectName(u"labelBox_tE_ChooseScope")
        self.labelBox_tE_ChooseScope.setFont(font)
        self.labelBox_tE_ChooseScope.setStyleSheet(u"")

        self.tE_ChooseScope.addWidget(self.labelBox_tE_ChooseScope)

        self.comboBox_tE_ChooseScope = QComboBox(self.scrollAreaWidgetContents_tE)
        self.comboBox_tE_ChooseScope.setObjectName(u"comboBox_tE_ChooseScope")
        self.comboBox_tE_ChooseScope.setFont(font)
        self.comboBox_tE_ChooseScope.setAutoFillBackground(False)
        self.comboBox_tE_ChooseScope.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_tE_ChooseScope.setIconSize(QSize(16, 16))
        self.comboBox_tE_ChooseScope.setFrame(True)

        self.tE_ChooseScope.addWidget(self.comboBox_tE_ChooseScope)


        self.tE_LeftColumn.addLayout(self.tE_ChooseScope)

        self.tE_Filter = QVBoxLayout()
        self.tE_Filter.setSpacing(0)
        self.tE_Filter.setObjectName(u"tE_Filter")
        self.labelBox_tE_Filter = QLabel(self.scrollAreaWidgetContents_tE)
        self.labelBox_tE_Filter.setObjectName(u"labelBox_tE_Filter")
        self.labelBox_tE_Filter.setFont(font)
        self.labelBox_tE_Filter.setStyleSheet(u"")

        self.tE_Filter.addWidget(self.labelBox_tE_Filter)

        self.horizontalLayout_tE_Filter = QHBoxLayout()
        self.horizontalLayout_tE_Filter.setSpacing(0)
        self.horizontalLayout_tE_Filter.setObjectName(u"horizontalLayout_tE_Filter")
        self.lineEdit_tE_Filter = QLineEdit(self.scrollAreaWidgetContents_tE)
        self.lineEdit_tE_Filter.setObjectName(u"lineEdit_tE_Filter")
        self.lineEdit_tE_Filter.setMinimumSize(QSize(0, 30))
        self.lineEdit_tE_Filter.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_tE_Filter.addWidget(self.lineEdit_tE_Filter)

        self.pushButton_tE_Filter = QPushButton(self.scrollAreaWidgetContents_tE)
        self.pushButton_tE_Filter.setObjectName(u"pushButton_tE_Filter")
        self.pushButton_tE_Filter.setMinimumSize(QSize(30, 30))
        self.pushButton_tE_Filter.setFont(font)
        self.pushButton_tE_Filter.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_tE_Filter.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pushButton_tE_Filter.setIcon(icon)
        self.pushButton_tE_Filter.setIconSize(QSize(16, 16))

        self.horizontalLayout_tE_Filter.addWidget(self.pushButton_tE_Filter)


        self.tE_Filter.addLayout(self.horizontalLayout_tE_Filter)


        self.tE_LeftColumn.addLayout(self.tE_Filter)

        self.tE_ChooseTag = QVBoxLayout()
        self.tE_ChooseTag.setSpacing(0)
        self.tE_ChooseTag.setObjectName(u"tE_ChooseTag")
        self.labelBox_tE_ChooseTag = QLabel(self.scrollAreaWidgetContents_tE)
        self.labelBox_tE_ChooseTag.setObjectName(u"labelBox_tE_ChooseTag")
        self.labelBox_tE_ChooseTag.setFont(font)
        self.labelBox_tE_ChooseTag.setStyleSheet(u"")

        self.tE_ChooseTag.addWidget(self.labelBox_tE_ChooseTag)

        self.listWidget_tE_ChooseTag = QListWidget(self.scrollAreaWidgetContents_tE)
        self.listWidget_tE_ChooseTag.setObjectName(u"listWidget_tE_ChooseTag")
        self.listWidget_tE_ChooseTag.setMinimumSize(QSize(0, 80))
        self.listWidget_tE_ChooseTag.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.tE_ChooseTag.addWidget(self.listWidget_tE_ChooseTag)


        self.tE_LeftColumn.addLayout(self.tE_ChooseTag)


        self.horizontalLayout_7.addLayout(self.tE_LeftColumn)

        self.tE_RightColumn = QVBoxLayout()
        self.tE_RightColumn.setObjectName(u"tE_RightColumn")
        self.tE_TagTree = QVBoxLayout()
        self.tE_TagTree.setSpacing(0)
        self.tE_TagTree.setObjectName(u"tE_TagTree")
        self.horizontalLayout_te_TagTree = QHBoxLayout()
        self.horizontalLayout_te_TagTree.setObjectName(u"horizontalLayout_te_TagTree")
        self.labelBox_tE_TagTree = QLabel(self.scrollAreaWidgetContents_tE)
        self.labelBox_tE_TagTree.setObjectName(u"labelBox_tE_TagTree")
        self.labelBox_tE_TagTree.setFont(font)
        self.labelBox_tE_TagTree.setStyleSheet(u"")

        self.horizontalLayout_te_TagTree.addWidget(self.labelBox_tE_TagTree)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_te_TagTree.addItem(self.horizontalSpacer)

        self.pushButton_tE_Expand = QPushButton(self.scrollAreaWidgetContents_tE)
        self.pushButton_tE_Expand.setObjectName(u"pushButton_tE_Expand")
        self.pushButton_tE_Expand.setMinimumSize(QSize(75, 15))
        self.pushButton_tE_Expand.setFont(font)
        self.pushButton_tE_Expand.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_tE_Expand.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_te_TagTree.addWidget(self.pushButton_tE_Expand)

        self.pushButton_tE_Collapse = QPushButton(self.scrollAreaWidgetContents_tE)
        self.pushButton_tE_Collapse.setObjectName(u"pushButton_tE_Collapse")
        self.pushButton_tE_Collapse.setMinimumSize(QSize(75, 15))
        self.pushButton_tE_Collapse.setFont(font)
        self.pushButton_tE_Collapse.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_tE_Collapse.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_te_TagTree.addWidget(self.pushButton_tE_Collapse)


        self.tE_TagTree.addLayout(self.horizontalLayout_te_TagTree)

        self.treeView_tE_TagTree = QTreeView(self.scrollAreaWidgetContents_tE)
        self.treeView_tE_TagTree.setObjectName(u"treeView_tE_TagTree")
        self.treeView_tE_TagTree.setMinimumSize(QSize(500, 0))
        self.treeView_tE_TagTree.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.tE_TagTree.addWidget(self.treeView_tE_TagTree)


        self.tE_RightColumn.addLayout(self.tE_TagTree)

        self.tE_Export = QHBoxLayout()
        self.tE_Export.setObjectName(u"tE_Export")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tE_Export.addItem(self.horizontalSpacer_2)

        self.horizontalFrame = QFrame(self.scrollAreaWidgetContents_tE)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.tE_Options_group = QVBoxLayout(self.horizontalFrame)
        self.tE_Options_group.setSpacing(2)
        self.tE_Options_group.setObjectName(u"tE_Options_group")
        self.tE_Options_group.setSizeConstraint(QLayout.SetMinimumSize)
        self.checkBox_tE_PrintHeaders = QCheckBox(self.horizontalFrame)
        self.checkBox_tE_PrintHeaders.setObjectName(u"checkBox_tE_PrintHeaders")
        self.checkBox_tE_PrintHeaders.setChecked(True)

        self.tE_Options_group.addWidget(self.checkBox_tE_PrintHeaders)

        self.checkBox_tE_ConcatenatePath = QCheckBox(self.horizontalFrame)
        self.checkBox_tE_ConcatenatePath.setObjectName(u"checkBox_tE_ConcatenatePath")
        self.checkBox_tE_ConcatenatePath.setChecked(True)

        self.tE_Options_group.addWidget(self.checkBox_tE_ConcatenatePath)


        self.tE_Export.addWidget(self.horizontalFrame, 0, Qt.AlignTop)

        self.tE_RadioButton_group = QGroupBox(self.scrollAreaWidgetContents_tE)
        self.tE_RadioButton_group.setObjectName(u"tE_RadioButton_group")
        self.tE_RadioButton_group.setStyleSheet(u"border: rgb(255,0,0);")
        self.tE_RadioButtons = QVBoxLayout(self.tE_RadioButton_group)
        self.tE_RadioButtons.setSpacing(2)
        self.tE_RadioButtons.setObjectName(u"tE_RadioButtons")
        self.radioButton_tE_PL = QRadioButton(self.tE_RadioButton_group)
        self.radioButton_tE_PL.setObjectName(u"radioButton_tE_PL")
        self.radioButton_tE_PL.setStyleSheet(u"")
        self.radioButton_tE_PL.setChecked(True)

        self.tE_RadioButtons.addWidget(self.radioButton_tE_PL)

        self.radioButton_tE_GFS = QRadioButton(self.tE_RadioButton_group)
        self.radioButton_tE_GFS.setObjectName(u"radioButton_tE_GFS")
        self.radioButton_tE_GFS.setStyleSheet(u"")

        self.tE_RadioButtons.addWidget(self.radioButton_tE_GFS)

        self.radioButton_tE_RU = QRadioButton(self.tE_RadioButton_group)
        self.radioButton_tE_RU.setObjectName(u"radioButton_tE_RU")
        self.radioButton_tE_RU.setStyleSheet(u"")

        self.tE_RadioButtons.addWidget(self.radioButton_tE_RU)

        self.radioButton_tE_UTF = QRadioButton(self.tE_RadioButton_group)
        self.radioButton_tE_UTF.setObjectName(u"radioButton_tE_UTF")
        self.radioButton_tE_UTF.setStyleSheet(u"")

        self.tE_RadioButtons.addWidget(self.radioButton_tE_UTF)

        self.horizontalLayout_tE_RadioButtons = QHBoxLayout()
        self.horizontalLayout_tE_RadioButtons.setSpacing(0)
        self.horizontalLayout_tE_RadioButtons.setObjectName(u"horizontalLayout_tE_RadioButtons")
        self.horizontalLayout_tE_RadioButtons.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.radioButton_tE_Custom = QRadioButton(self.tE_RadioButton_group)
        self.radioButton_tE_Custom.setObjectName(u"radioButton_tE_Custom")
        self.radioButton_tE_Custom.setMaximumSize(QSize(22, 16777215))
        self.radioButton_tE_Custom.setStyleSheet(u"")

        self.horizontalLayout_tE_RadioButtons.addWidget(self.radioButton_tE_Custom)

        self.lineEdit_tE_RadioButton_Custom = QLineEdit(self.tE_RadioButton_group)
        self.lineEdit_tE_RadioButton_Custom.setObjectName(u"lineEdit_tE_RadioButton_Custom")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_tE_RadioButton_Custom.sizePolicy().hasHeightForWidth())
        self.lineEdit_tE_RadioButton_Custom.setSizePolicy(sizePolicy3)
        self.lineEdit_tE_RadioButton_Custom.setMinimumSize(QSize(0, 0))
        self.lineEdit_tE_RadioButton_Custom.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_tE_RadioButtons.addWidget(self.lineEdit_tE_RadioButton_Custom)


        self.tE_RadioButtons.addLayout(self.horizontalLayout_tE_RadioButtons)


        self.tE_Export.addWidget(self.tE_RadioButton_group)

        self.te_ExportImport_layout = QVBoxLayout()
        self.te_ExportImport_layout.setSpacing(12)
        self.te_ExportImport_layout.setObjectName(u"te_ExportImport_layout")
        self.te_ExportImport_layout.setContentsMargins(-1, 9, -1, 9)
        self.pushButton_tE_Export = QPushButton(self.scrollAreaWidgetContents_tE)
        self.pushButton_tE_Export.setObjectName(u"pushButton_tE_Export")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_tE_Export.sizePolicy().hasHeightForWidth())
        self.pushButton_tE_Export.setSizePolicy(sizePolicy4)
        self.pushButton_tE_Export.setMinimumSize(QSize(150, 24))
        self.pushButton_tE_Export.setFont(font)
        self.pushButton_tE_Export.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_tE_Export.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_tE_Export.setFlat(False)

        self.te_ExportImport_layout.addWidget(self.pushButton_tE_Export)

        self.pushButton_tE_Import = QPushButton(self.scrollAreaWidgetContents_tE)
        self.pushButton_tE_Import.setObjectName(u"pushButton_tE_Import")
        sizePolicy4.setHeightForWidth(self.pushButton_tE_Import.sizePolicy().hasHeightForWidth())
        self.pushButton_tE_Import.setSizePolicy(sizePolicy4)
        self.pushButton_tE_Import.setMinimumSize(QSize(150, 24))
        self.pushButton_tE_Import.setFont(font)
        self.pushButton_tE_Import.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_tE_Import.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_tE_Import.setFlat(False)

        self.te_ExportImport_layout.addWidget(self.pushButton_tE_Import)


        self.tE_Export.addLayout(self.te_ExportImport_layout)


        self.tE_RightColumn.addLayout(self.tE_Export)


        self.horizontalLayout_7.addLayout(self.tE_RightColumn)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.scrollArea_tE.setWidget(self.scrollAreaWidgetContents_tE)

        self.verticalLayout_16.addWidget(self.scrollArea_tE)

        self.stackedWidget.addWidget(self.page_tagExport)
        self.page_strConverter = QWidget()
        self.page_strConverter.setObjectName(u"page_strConverter")
        self.verticalLayout = QVBoxLayout(self.page_strConverter)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_tsC = QScrollArea(self.page_strConverter)
        self.scrollArea_tsC.setObjectName(u"scrollArea_tsC")
        self.scrollArea_tsC.setWidgetResizable(True)
        self.scrollAreaWidgetContents_tsC = QWidget()
        self.scrollAreaWidgetContents_tsC.setObjectName(u"scrollAreaWidgetContents_tsC")
        self.scrollAreaWidgetContents_tsC.setGeometry(QRect(0, 0, 388, 349))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_tsC)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.tsC_TextRow = QHBoxLayout()
        self.tsC_TextRow.setObjectName(u"tsC_TextRow")
        self.tsC_SimpleText = QVBoxLayout()
        self.tsC_SimpleText.setSpacing(0)
        self.tsC_SimpleText.setObjectName(u"tsC_SimpleText")
        self.label_tsC_SimpleText = QLabel(self.scrollAreaWidgetContents_tsC)
        self.label_tsC_SimpleText.setObjectName(u"label_tsC_SimpleText")

        self.tsC_SimpleText.addWidget(self.label_tsC_SimpleText)

        self.textEdit_tsC_SimpleText = QPlainTextEdit(self.scrollAreaWidgetContents_tsC)
        self.textEdit_tsC_SimpleText.setObjectName(u"textEdit_tsC_SimpleText")
        self.textEdit_tsC_SimpleText.setMinimumSize(QSize(200, 100))
        self.textEdit_tsC_SimpleText.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.tsC_SimpleText.addWidget(self.textEdit_tsC_SimpleText)


        self.tsC_TextRow.addLayout(self.tsC_SimpleText)

        self.tsC_TextButtons = QVBoxLayout()
        self.tsC_TextButtons.setObjectName(u"tsC_TextButtons")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.tsC_TextButtons.addItem(self.verticalSpacer_4)

        self.pushButton_tsC_CopyText = QPushButton(self.scrollAreaWidgetContents_tsC)
        self.pushButton_tsC_CopyText.setObjectName(u"pushButton_tsC_CopyText")
        sizePolicy4.setHeightForWidth(self.pushButton_tsC_CopyText.sizePolicy().hasHeightForWidth())
        self.pushButton_tsC_CopyText.setSizePolicy(sizePolicy4)
        self.pushButton_tsC_CopyText.setMinimumSize(QSize(158, 24))
        self.pushButton_tsC_CopyText.setFont(font)
        self.pushButton_tsC_CopyText.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_tsC_CopyText.setStyleSheet(u"")
        self.pushButton_tsC_CopyText.setFlat(False)

        self.tsC_TextButtons.addWidget(self.pushButton_tsC_CopyText)

        self.pushButton_tsC_PasteText = QPushButton(self.scrollAreaWidgetContents_tsC)
        self.pushButton_tsC_PasteText.setObjectName(u"pushButton_tsC_PasteText")
        sizePolicy4.setHeightForWidth(self.pushButton_tsC_PasteText.sizePolicy().hasHeightForWidth())
        self.pushButton_tsC_PasteText.setSizePolicy(sizePolicy4)
        self.pushButton_tsC_PasteText.setMinimumSize(QSize(158, 24))
        self.pushButton_tsC_PasteText.setFont(font)
        self.pushButton_tsC_PasteText.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_tsC_PasteText.setStyleSheet(u"")
        self.pushButton_tsC_PasteText.setFlat(False)

        self.tsC_TextButtons.addWidget(self.pushButton_tsC_PasteText)


        self.tsC_TextRow.addLayout(self.tsC_TextButtons)


        self.verticalLayout_20.addLayout(self.tsC_TextRow)

        self.tsC_RSLRow = QHBoxLayout()
        self.tsC_RSLRow.setObjectName(u"tsC_RSLRow")
        self.tsC_RSLogixText = QVBoxLayout()
        self.tsC_RSLogixText.setSpacing(0)
        self.tsC_RSLogixText.setObjectName(u"tsC_RSLogixText")
        self.label_tsC_RSLogixText = QLabel(self.scrollAreaWidgetContents_tsC)
        self.label_tsC_RSLogixText.setObjectName(u"label_tsC_RSLogixText")

        self.tsC_RSLogixText.addWidget(self.label_tsC_RSLogixText)

        self.textEdit_tsC_RSLogixText = QPlainTextEdit(self.scrollAreaWidgetContents_tsC)
        self.textEdit_tsC_RSLogixText.setObjectName(u"textEdit_tsC_RSLogixText")
        self.textEdit_tsC_RSLogixText.setMinimumSize(QSize(200, 100))
        self.textEdit_tsC_RSLogixText.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.tsC_RSLogixText.addWidget(self.textEdit_tsC_RSLogixText)


        self.tsC_RSLRow.addLayout(self.tsC_RSLogixText)

        self.tsC_RSLButtons = QVBoxLayout()
        self.tsC_RSLButtons.setObjectName(u"tsC_RSLButtons")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.tsC_RSLButtons.addItem(self.verticalSpacer_5)

        self.tsC_RadioButton_group = QGroupBox(self.scrollAreaWidgetContents_tsC)
        self.tsC_RadioButton_group.setObjectName(u"tsC_RadioButton_group")
        self.tsC_RadioButton_group.setStyleSheet(u"border: rgb(255,0,0);")
        self.tE_RadioButtons_3 = QVBoxLayout(self.tsC_RadioButton_group)
        self.tE_RadioButtons_3.setSpacing(2)
        self.tE_RadioButtons_3.setObjectName(u"tE_RadioButtons_3")
        self.radioButton_tsC_PL = QRadioButton(self.tsC_RadioButton_group)
        self.radioButton_tsC_PL.setObjectName(u"radioButton_tsC_PL")
        self.radioButton_tsC_PL.setStyleSheet(u"")
        self.radioButton_tsC_PL.setChecked(True)

        self.tE_RadioButtons_3.addWidget(self.radioButton_tsC_PL)

        self.radioButton_tsC_GFS = QRadioButton(self.tsC_RadioButton_group)
        self.radioButton_tsC_GFS.setObjectName(u"radioButton_tsC_GFS")
        self.radioButton_tsC_GFS.setStyleSheet(u"")

        self.tE_RadioButtons_3.addWidget(self.radioButton_tsC_GFS)

        self.radioButton_tsC_RU = QRadioButton(self.tsC_RadioButton_group)
        self.radioButton_tsC_RU.setObjectName(u"radioButton_tsC_RU")
        self.radioButton_tsC_RU.setStyleSheet(u"")

        self.tE_RadioButtons_3.addWidget(self.radioButton_tsC_RU)

        self.radioButton_tsC_UTF = QRadioButton(self.tsC_RadioButton_group)
        self.radioButton_tsC_UTF.setObjectName(u"radioButton_tsC_UTF")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.radioButton_tsC_UTF.sizePolicy().hasHeightForWidth())
        self.radioButton_tsC_UTF.setSizePolicy(sizePolicy5)
        self.radioButton_tsC_UTF.setStyleSheet(u"")

        self.tE_RadioButtons_3.addWidget(self.radioButton_tsC_UTF)

        self.horizontalLayout_tsC_RadioButtons = QHBoxLayout()
        self.horizontalLayout_tsC_RadioButtons.setSpacing(0)
        self.horizontalLayout_tsC_RadioButtons.setObjectName(u"horizontalLayout_tsC_RadioButtons")
        self.horizontalLayout_tsC_RadioButtons.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.radioButton_tsC_Custom = QRadioButton(self.tsC_RadioButton_group)
        self.radioButton_tsC_Custom.setObjectName(u"radioButton_tsC_Custom")
        self.radioButton_tsC_Custom.setMaximumSize(QSize(22, 16777215))
        self.radioButton_tsC_Custom.setStyleSheet(u"")

        self.horizontalLayout_tsC_RadioButtons.addWidget(self.radioButton_tsC_Custom)

        self.lineEdit_tsC_RadioButton_Custom = QLineEdit(self.tsC_RadioButton_group)
        self.lineEdit_tsC_RadioButton_Custom.setObjectName(u"lineEdit_tsC_RadioButton_Custom")
        sizePolicy3.setHeightForWidth(self.lineEdit_tsC_RadioButton_Custom.sizePolicy().hasHeightForWidth())
        self.lineEdit_tsC_RadioButton_Custom.setSizePolicy(sizePolicy3)
        self.lineEdit_tsC_RadioButton_Custom.setMinimumSize(QSize(0, 0))
        self.lineEdit_tsC_RadioButton_Custom.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_tsC_RadioButtons.addWidget(self.lineEdit_tsC_RadioButton_Custom)


        self.tE_RadioButtons_3.addLayout(self.horizontalLayout_tsC_RadioButtons)


        self.tsC_RSLButtons.addWidget(self.tsC_RadioButton_group)

        self.pushButton_tsC_CopyRSL = QPushButton(self.scrollAreaWidgetContents_tsC)
        self.pushButton_tsC_CopyRSL.setObjectName(u"pushButton_tsC_CopyRSL")
        sizePolicy4.setHeightForWidth(self.pushButton_tsC_CopyRSL.sizePolicy().hasHeightForWidth())
        self.pushButton_tsC_CopyRSL.setSizePolicy(sizePolicy4)
        self.pushButton_tsC_CopyRSL.setMinimumSize(QSize(158, 24))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.pushButton_tsC_CopyRSL.setPalette(palette)
        self.pushButton_tsC_CopyRSL.setFont(font)
        self.pushButton_tsC_CopyRSL.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_tsC_CopyRSL.setStyleSheet(u"")
        self.pushButton_tsC_CopyRSL.setFlat(False)

        self.tsC_RSLButtons.addWidget(self.pushButton_tsC_CopyRSL)

        self.pushButton_tsC_PasteRSL = QPushButton(self.scrollAreaWidgetContents_tsC)
        self.pushButton_tsC_PasteRSL.setObjectName(u"pushButton_tsC_PasteRSL")
        sizePolicy4.setHeightForWidth(self.pushButton_tsC_PasteRSL.sizePolicy().hasHeightForWidth())
        self.pushButton_tsC_PasteRSL.setSizePolicy(sizePolicy4)
        self.pushButton_tsC_PasteRSL.setMinimumSize(QSize(150, 24))
        self.pushButton_tsC_PasteRSL.setFont(font)
        self.pushButton_tsC_PasteRSL.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_tsC_PasteRSL.setStyleSheet(u"")
        self.pushButton_tsC_PasteRSL.setFlat(False)

        self.tsC_RSLButtons.addWidget(self.pushButton_tsC_PasteRSL)


        self.tsC_RSLRow.addLayout(self.tsC_RSLButtons)


        self.verticalLayout_20.addLayout(self.tsC_RSLRow)

        self.scrollArea_tsC.setWidget(self.scrollAreaWidgetContents_tsC)

        self.verticalLayout.addWidget(self.scrollArea_tsC)

        self.stackedWidget.addWidget(self.page_strConverter)
        self.page_rungGenerator = QWidget()
        self.page_rungGenerator.setObjectName(u"page_rungGenerator")
        self.verticalLayout_17 = QVBoxLayout(self.page_rungGenerator)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.scrollArea_rG = QScrollArea(self.page_rungGenerator)
        self.scrollArea_rG.setObjectName(u"scrollArea_rG")
        self.scrollArea_rG.setWidgetResizable(True)
        self.scrollAreaWidgetContents_rG = QWidget()
        self.scrollAreaWidgetContents_rG.setObjectName(u"scrollAreaWidgetContents_rG")
        self.scrollAreaWidgetContents_rG.setGeometry(QRect(0, 0, 950, 424))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_rG)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.rG_header = QHBoxLayout()
        self.rG_header.setObjectName(u"rG_header")
        self.rG_config_OpenFile = QGridLayout()
        self.rG_config_OpenFile.setObjectName(u"rG_config_OpenFile")
        self.rG_config_OpenFile.setVerticalSpacing(0)
        self.lineEdit_rG_config_OpenFile = QLineEdit(self.scrollAreaWidgetContents_rG)
        self.lineEdit_rG_config_OpenFile.setObjectName(u"lineEdit_rG_config_OpenFile")
        self.lineEdit_rG_config_OpenFile.setMinimumSize(QSize(0, 30))
        self.lineEdit_rG_config_OpenFile.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.rG_config_OpenFile.addWidget(self.lineEdit_rG_config_OpenFile, 1, 0, 1, 1)

        self.pushButton_rG_config_OpenFile = QPushButton(self.scrollAreaWidgetContents_rG)
        self.pushButton_rG_config_OpenFile.setObjectName(u"pushButton_rG_config_OpenFile")
        self.pushButton_rG_config_OpenFile.setMinimumSize(QSize(100, 30))
        self.pushButton_rG_config_OpenFile.setFont(font)
        self.pushButton_rG_config_OpenFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_rG_config_OpenFile.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_rG_config_OpenFile.setIcon(icon4)

        self.rG_config_OpenFile.addWidget(self.pushButton_rG_config_OpenFile, 1, 1, 1, 1)

        self.labelBox_rG_config_OpenFile = QLabel(self.scrollAreaWidgetContents_rG)
        self.labelBox_rG_config_OpenFile.setObjectName(u"labelBox_rG_config_OpenFile")
        self.labelBox_rG_config_OpenFile.setFont(font)
        self.labelBox_rG_config_OpenFile.setStyleSheet(u"")

        self.rG_config_OpenFile.addWidget(self.labelBox_rG_config_OpenFile, 0, 0, 1, 2)


        self.rG_header.addLayout(self.rG_config_OpenFile)

        self.pushButton_rG_preparePage = QPushButton(self.scrollAreaWidgetContents_rG)
        self.pushButton_rG_preparePage.setObjectName(u"pushButton_rG_preparePage")
        sizePolicy4.setHeightForWidth(self.pushButton_rG_preparePage.sizePolicy().hasHeightForWidth())
        self.pushButton_rG_preparePage.setSizePolicy(sizePolicy4)
        self.pushButton_rG_preparePage.setMinimumSize(QSize(105, 24))
        self.pushButton_rG_preparePage.setFont(font)
        self.pushButton_rG_preparePage.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_rG_preparePage.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_rG_preparePage.setFlat(False)

        self.rG_header.addWidget(self.pushButton_rG_preparePage)

        self.pushButton_rG_importPage = QPushButton(self.scrollAreaWidgetContents_rG)
        self.pushButton_rG_importPage.setObjectName(u"pushButton_rG_importPage")
        sizePolicy4.setHeightForWidth(self.pushButton_rG_importPage.sizePolicy().hasHeightForWidth())
        self.pushButton_rG_importPage.setSizePolicy(sizePolicy4)
        self.pushButton_rG_importPage.setMinimumSize(QSize(105, 24))
        self.pushButton_rG_importPage.setFont(font)
        self.pushButton_rG_importPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_rG_importPage.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_rG_importPage.setFlat(False)

        self.rG_header.addWidget(self.pushButton_rG_importPage)


        self.verticalLayout_26.addLayout(self.rG_header)

        self.stackedWidget_rG_pages = QStackedWidget(self.scrollAreaWidgetContents_rG)
        self.stackedWidget_rG_pages.setObjectName(u"stackedWidget_rG_pages")
        self.stackedWidget_rG_pages.setLineWidth(1)
        self.page_rG_prepareCSV = QWidget()
        self.page_rG_prepareCSV.setObjectName(u"page_rG_prepareCSV")
        self.horizontalLayout_8 = QHBoxLayout(self.page_rG_prepareCSV)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.rG_prepareOptions = QVBoxLayout()
        self.rG_prepareOptions.setObjectName(u"rG_prepareOptions")
        self.rG_rungsTemplate = QGridLayout()
        self.rG_rungsTemplate.setObjectName(u"rG_rungsTemplate")
        self.rG_rungsTemplate.setVerticalSpacing(0)
        self.lineEdit_rG_rungs_OpenFile = QLineEdit(self.page_rG_prepareCSV)
        self.lineEdit_rG_rungs_OpenFile.setObjectName(u"lineEdit_rG_rungs_OpenFile")
        self.lineEdit_rG_rungs_OpenFile.setMinimumSize(QSize(0, 30))
        self.lineEdit_rG_rungs_OpenFile.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.rG_rungsTemplate.addWidget(self.lineEdit_rG_rungs_OpenFile, 1, 0, 1, 1)

        self.pushButton_rG_rungs_OpenFile = QPushButton(self.page_rG_prepareCSV)
        self.pushButton_rG_rungs_OpenFile.setObjectName(u"pushButton_rG_rungs_OpenFile")
        self.pushButton_rG_rungs_OpenFile.setMinimumSize(QSize(100, 30))
        self.pushButton_rG_rungs_OpenFile.setFont(font)
        self.pushButton_rG_rungs_OpenFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_rG_rungs_OpenFile.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_rG_rungs_OpenFile.setIcon(icon4)

        self.rG_rungsTemplate.addWidget(self.pushButton_rG_rungs_OpenFile, 1, 1, 1, 1)

        self.labelBox_rG_rungs_OpenFile = QLabel(self.page_rG_prepareCSV)
        self.labelBox_rG_rungs_OpenFile.setObjectName(u"labelBox_rG_rungs_OpenFile")
        self.labelBox_rG_rungs_OpenFile.setFont(font)
        self.labelBox_rG_rungs_OpenFile.setStyleSheet(u"")

        self.rG_rungsTemplate.addWidget(self.labelBox_rG_rungs_OpenFile, 0, 0, 1, 2)


        self.rG_prepareOptions.addLayout(self.rG_rungsTemplate)

        self.rG_faultTemplate = QGridLayout()
        self.rG_faultTemplate.setObjectName(u"rG_faultTemplate")
        self.rG_faultTemplate.setVerticalSpacing(0)
        self.lineEdit_rG_fault_OpenFile = QLineEdit(self.page_rG_prepareCSV)
        self.lineEdit_rG_fault_OpenFile.setObjectName(u"lineEdit_rG_fault_OpenFile")
        self.lineEdit_rG_fault_OpenFile.setMinimumSize(QSize(0, 30))
        self.lineEdit_rG_fault_OpenFile.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.rG_faultTemplate.addWidget(self.lineEdit_rG_fault_OpenFile, 1, 0, 1, 1)

        self.labelBox_rG_fault_OpenFile = QLabel(self.page_rG_prepareCSV)
        self.labelBox_rG_fault_OpenFile.setObjectName(u"labelBox_rG_fault_OpenFile")
        self.labelBox_rG_fault_OpenFile.setFont(font)
        self.labelBox_rG_fault_OpenFile.setStyleSheet(u"")

        self.rG_faultTemplate.addWidget(self.labelBox_rG_fault_OpenFile, 0, 0, 1, 2)

        self.pushButton_rG_fault_OpenFile = QPushButton(self.page_rG_prepareCSV)
        self.pushButton_rG_fault_OpenFile.setObjectName(u"pushButton_rG_fault_OpenFile")
        self.pushButton_rG_fault_OpenFile.setMinimumSize(QSize(100, 30))
        self.pushButton_rG_fault_OpenFile.setFont(font)
        self.pushButton_rG_fault_OpenFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_rG_fault_OpenFile.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_rG_fault_OpenFile.setIcon(icon4)

        self.rG_faultTemplate.addWidget(self.pushButton_rG_fault_OpenFile, 1, 1, 1, 1)


        self.rG_prepareOptions.addLayout(self.rG_faultTemplate)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.rG_prepareOptions.addItem(self.verticalSpacer_3)

        self.pushButton_rG_saveConfiguration = QPushButton(self.page_rG_prepareCSV)
        self.pushButton_rG_saveConfiguration.setObjectName(u"pushButton_rG_saveConfiguration")
        sizePolicy4.setHeightForWidth(self.pushButton_rG_saveConfiguration.sizePolicy().hasHeightForWidth())
        self.pushButton_rG_saveConfiguration.setSizePolicy(sizePolicy4)
        self.pushButton_rG_saveConfiguration.setMinimumSize(QSize(150, 24))
        self.pushButton_rG_saveConfiguration.setFont(font)
        self.pushButton_rG_saveConfiguration.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_rG_saveConfiguration.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_rG_saveConfiguration.setFlat(False)

        self.rG_prepareOptions.addWidget(self.pushButton_rG_saveConfiguration)

        self.pushButton_rG_exportCSV = QPushButton(self.page_rG_prepareCSV)
        self.pushButton_rG_exportCSV.setObjectName(u"pushButton_rG_exportCSV")
        sizePolicy4.setHeightForWidth(self.pushButton_rG_exportCSV.sizePolicy().hasHeightForWidth())
        self.pushButton_rG_exportCSV.setSizePolicy(sizePolicy4)
        self.pushButton_rG_exportCSV.setMinimumSize(QSize(150, 24))
        self.pushButton_rG_exportCSV.setFont(font)
        self.pushButton_rG_exportCSV.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_rG_exportCSV.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_rG_exportCSV.setFlat(False)

        self.rG_prepareOptions.addWidget(self.pushButton_rG_exportCSV)


        self.horizontalLayout_8.addLayout(self.rG_prepareOptions)

        self.rG_tree_layout = QVBoxLayout()
        self.rG_tree_layout.setObjectName(u"rG_tree_layout")
        self.rG_tree_header = QHBoxLayout()
        self.rG_tree_header.setObjectName(u"rG_tree_header")
        self.labelBox_rG_treeHeader = QLabel(self.page_rG_prepareCSV)
        self.labelBox_rG_treeHeader.setObjectName(u"labelBox_rG_treeHeader")
        self.labelBox_rG_treeHeader.setFont(font)
        self.labelBox_rG_treeHeader.setStyleSheet(u"")

        self.rG_tree_header.addWidget(self.labelBox_rG_treeHeader)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.rG_tree_header.addItem(self.horizontalSpacer_4)

        self.pushButton_rG_appear = QPushButton(self.page_rG_prepareCSV)
        self.pushButton_rG_appear.setObjectName(u"pushButton_rG_appear")
        self.pushButton_rG_appear.setMinimumSize(QSize(75, 15))
        self.pushButton_rG_appear.setFont(font)
        self.pushButton_rG_appear.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_rG_appear.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.rG_tree_header.addWidget(self.pushButton_rG_appear)

        self.pushButton_rG_alphabetical = QPushButton(self.page_rG_prepareCSV)
        self.pushButton_rG_alphabetical.setObjectName(u"pushButton_rG_alphabetical")
        self.pushButton_rG_alphabetical.setMinimumSize(QSize(75, 15))
        self.pushButton_rG_alphabetical.setFont(font)
        self.pushButton_rG_alphabetical.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_rG_alphabetical.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.rG_tree_header.addWidget(self.pushButton_rG_alphabetical)


        self.rG_tree_layout.addLayout(self.rG_tree_header)

        self.treeView_trG = QTreeView(self.page_rG_prepareCSV)
        self.treeView_trG.setObjectName(u"treeView_trG")

        self.rG_tree_layout.addWidget(self.treeView_trG)


        self.horizontalLayout_8.addLayout(self.rG_tree_layout)

        self.stackedWidget_rG_pages.addWidget(self.page_rG_prepareCSV)
        self.page_rG_importCSV = QWidget()
        self.page_rG_importCSV.setObjectName(u"page_rG_importCSV")
        self.horizontalLayout_9 = QHBoxLayout(self.page_rG_importCSV)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.rG_import_leftColumn = QVBoxLayout()
        self.rG_import_leftColumn.setObjectName(u"rG_import_leftColumn")
        self.rG_chooseProgram = QVBoxLayout()
        self.rG_chooseProgram.setSpacing(0)
        self.rG_chooseProgram.setObjectName(u"rG_chooseProgram")
        self.labelBox_rG_chooseProgram = QLabel(self.page_rG_importCSV)
        self.labelBox_rG_chooseProgram.setObjectName(u"labelBox_rG_chooseProgram")
        self.labelBox_rG_chooseProgram.setFont(font)
        self.labelBox_rG_chooseProgram.setStyleSheet(u"")

        self.rG_chooseProgram.addWidget(self.labelBox_rG_chooseProgram)

        self.comboBox_rG_chooseProgram = QComboBox(self.page_rG_importCSV)
        self.comboBox_rG_chooseProgram.setObjectName(u"comboBox_rG_chooseProgram")
        self.comboBox_rG_chooseProgram.setFont(font)
        self.comboBox_rG_chooseProgram.setAutoFillBackground(False)
        self.comboBox_rG_chooseProgram.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_rG_chooseProgram.setIconSize(QSize(16, 16))
        self.comboBox_rG_chooseProgram.setFrame(True)

        self.rG_chooseProgram.addWidget(self.comboBox_rG_chooseProgram)


        self.rG_import_leftColumn.addLayout(self.rG_chooseProgram)

        self.rG_chooseRungsRoutine = QVBoxLayout()
        self.rG_chooseRungsRoutine.setSpacing(0)
        self.rG_chooseRungsRoutine.setObjectName(u"rG_chooseRungsRoutine")
        self.labelBox_rG_chooseRungsRoutine = QLabel(self.page_rG_importCSV)
        self.labelBox_rG_chooseRungsRoutine.setObjectName(u"labelBox_rG_chooseRungsRoutine")
        self.labelBox_rG_chooseRungsRoutine.setFont(font)
        self.labelBox_rG_chooseRungsRoutine.setStyleSheet(u"")

        self.rG_chooseRungsRoutine.addWidget(self.labelBox_rG_chooseRungsRoutine)

        self.comboBox_rG_chooseRungsRoutine = QComboBox(self.page_rG_importCSV)
        self.comboBox_rG_chooseRungsRoutine.setObjectName(u"comboBox_rG_chooseRungsRoutine")
        self.comboBox_rG_chooseRungsRoutine.setFont(font)
        self.comboBox_rG_chooseRungsRoutine.setAutoFillBackground(False)
        self.comboBox_rG_chooseRungsRoutine.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_rG_chooseRungsRoutine.setIconSize(QSize(16, 16))
        self.comboBox_rG_chooseRungsRoutine.setFrame(True)

        self.rG_chooseRungsRoutine.addWidget(self.comboBox_rG_chooseRungsRoutine)


        self.rG_import_leftColumn.addLayout(self.rG_chooseRungsRoutine)

        self.rG_rungs_rungNumber = QVBoxLayout()
        self.rG_rungs_rungNumber.setObjectName(u"rG_rungs_rungNumber")
        self.labelBox_rG_rungs_rungNumber = QLabel(self.page_rG_importCSV)
        self.labelBox_rG_rungs_rungNumber.setObjectName(u"labelBox_rG_rungs_rungNumber")
        self.labelBox_rG_rungs_rungNumber.setFont(font)
        self.labelBox_rG_rungs_rungNumber.setStyleSheet(u"")

        self.rG_rungs_rungNumber.addWidget(self.labelBox_rG_rungs_rungNumber)

        self.lineEdit_rG_rungs_rungNumber = QLineEdit(self.page_rG_importCSV)
        self.lineEdit_rG_rungs_rungNumber.setObjectName(u"lineEdit_rG_rungs_rungNumber")
        sizePolicy3.setHeightForWidth(self.lineEdit_rG_rungs_rungNumber.sizePolicy().hasHeightForWidth())
        self.lineEdit_rG_rungs_rungNumber.setSizePolicy(sizePolicy3)
        self.lineEdit_rG_rungs_rungNumber.setMinimumSize(QSize(0, 0))
        self.lineEdit_rG_rungs_rungNumber.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.rG_rungs_rungNumber.addWidget(self.lineEdit_rG_rungs_rungNumber)


        self.rG_import_leftColumn.addLayout(self.rG_rungs_rungNumber)

        self.rG_chooseFaultsRoutine = QVBoxLayout()
        self.rG_chooseFaultsRoutine.setSpacing(0)
        self.rG_chooseFaultsRoutine.setObjectName(u"rG_chooseFaultsRoutine")
        self.labelBox_rG_chooseFaultsRoutine = QLabel(self.page_rG_importCSV)
        self.labelBox_rG_chooseFaultsRoutine.setObjectName(u"labelBox_rG_chooseFaultsRoutine")
        self.labelBox_rG_chooseFaultsRoutine.setFont(font)
        self.labelBox_rG_chooseFaultsRoutine.setStyleSheet(u"")

        self.rG_chooseFaultsRoutine.addWidget(self.labelBox_rG_chooseFaultsRoutine)

        self.comboBox_rG_chooseFaultsRoutine = QComboBox(self.page_rG_importCSV)
        self.comboBox_rG_chooseFaultsRoutine.setObjectName(u"comboBox_rG_chooseFaultsRoutine")
        self.comboBox_rG_chooseFaultsRoutine.setFont(font)
        self.comboBox_rG_chooseFaultsRoutine.setAutoFillBackground(False)
        self.comboBox_rG_chooseFaultsRoutine.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_rG_chooseFaultsRoutine.setIconSize(QSize(16, 16))
        self.comboBox_rG_chooseFaultsRoutine.setFrame(True)

        self.rG_chooseFaultsRoutine.addWidget(self.comboBox_rG_chooseFaultsRoutine)


        self.rG_import_leftColumn.addLayout(self.rG_chooseFaultsRoutine)

        self.rG_faults_rungNumber = QVBoxLayout()
        self.rG_faults_rungNumber.setObjectName(u"rG_faults_rungNumber")
        self.labelBox_rG_faults_rungNumber = QLabel(self.page_rG_importCSV)
        self.labelBox_rG_faults_rungNumber.setObjectName(u"labelBox_rG_faults_rungNumber")
        self.labelBox_rG_faults_rungNumber.setFont(font)
        self.labelBox_rG_faults_rungNumber.setStyleSheet(u"")

        self.rG_faults_rungNumber.addWidget(self.labelBox_rG_faults_rungNumber)

        self.lineEdit_rG_faults_rungNumber = QLineEdit(self.page_rG_importCSV)
        self.lineEdit_rG_faults_rungNumber.setObjectName(u"lineEdit_rG_faults_rungNumber")
        sizePolicy3.setHeightForWidth(self.lineEdit_rG_faults_rungNumber.sizePolicy().hasHeightForWidth())
        self.lineEdit_rG_faults_rungNumber.setSizePolicy(sizePolicy3)
        self.lineEdit_rG_faults_rungNumber.setMinimumSize(QSize(0, 0))
        self.lineEdit_rG_faults_rungNumber.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.rG_faults_rungNumber.addWidget(self.lineEdit_rG_faults_rungNumber)


        self.rG_import_leftColumn.addLayout(self.rG_faults_rungNumber)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.rG_import_leftColumn.addItem(self.verticalSpacer_2)

        self.pushButton_rG_generateInProject = QPushButton(self.page_rG_importCSV)
        self.pushButton_rG_generateInProject.setObjectName(u"pushButton_rG_generateInProject")
        sizePolicy4.setHeightForWidth(self.pushButton_rG_generateInProject.sizePolicy().hasHeightForWidth())
        self.pushButton_rG_generateInProject.setSizePolicy(sizePolicy4)
        self.pushButton_rG_generateInProject.setMinimumSize(QSize(150, 24))
        self.pushButton_rG_generateInProject.setFont(font)
        self.pushButton_rG_generateInProject.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_rG_generateInProject.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_rG_generateInProject.setFlat(False)

        self.rG_import_leftColumn.addWidget(self.pushButton_rG_generateInProject)


        self.horizontalLayout_9.addLayout(self.rG_import_leftColumn)

        self.rG_import_rightColumn = QVBoxLayout()
        self.rG_import_rightColumn.setObjectName(u"rG_import_rightColumn")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.rG_import_rightColumn.addItem(self.verticalSpacer_6)

        self.pushButton_rG_generateExportFiles = QPushButton(self.page_rG_importCSV)
        self.pushButton_rG_generateExportFiles.setObjectName(u"pushButton_rG_generateExportFiles")
        sizePolicy4.setHeightForWidth(self.pushButton_rG_generateExportFiles.sizePolicy().hasHeightForWidth())
        self.pushButton_rG_generateExportFiles.setSizePolicy(sizePolicy4)
        self.pushButton_rG_generateExportFiles.setMinimumSize(QSize(150, 24))
        self.pushButton_rG_generateExportFiles.setFont(font)
        self.pushButton_rG_generateExportFiles.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_rG_generateExportFiles.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_rG_generateExportFiles.setFlat(False)

        self.rG_import_rightColumn.addWidget(self.pushButton_rG_generateExportFiles)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.rG_import_rightColumn.addItem(self.verticalSpacer_7)


        self.horizontalLayout_9.addLayout(self.rG_import_rightColumn)

        self.stackedWidget_rG_pages.addWidget(self.page_rG_importCSV)

        self.verticalLayout_26.addWidget(self.stackedWidget_rG_pages)

        self.scrollArea_rG.setWidget(self.scrollAreaWidgetContents_rG)

        self.verticalLayout_17.addWidget(self.scrollArea_rG)

        self.stackedWidget.addWidget(self.page_rungGenerator)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.contentSettings)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMinimumSize(QSize(0, 3))
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Plain)
        self.themeSettingsTopDetail.setLineWidth(3)
        self.themeSettingsTopDetail.setFrameShape(QFrame.HLine)

        self.verticalLayout_13.addWidget(self.themeSettingsTopDetail)

        self.pushButton_RB_ExportEncoding = QPushButton(self.contentSettings)
        self.pushButton_RB_ExportEncoding.setObjectName(u"pushButton_RB_ExportEncoding")
        sizePolicy.setHeightForWidth(self.pushButton_RB_ExportEncoding.sizePolicy().hasHeightForWidth())
        self.pushButton_RB_ExportEncoding.setSizePolicy(sizePolicy)
        self.pushButton_RB_ExportEncoding.setMinimumSize(QSize(0, 45))
        self.pushButton_RB_ExportEncoding.setFont(font)
        self.pushButton_RB_ExportEncoding.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_RB_ExportEncoding.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_RB_ExportEncoding.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-paragraph.png);")

        self.verticalLayout_13.addWidget(self.pushButton_RB_ExportEncoding)

        self.frame_RB_ExportEncoding = QFrame(self.contentSettings)
        self.frame_RB_ExportEncoding.setObjectName(u"frame_RB_ExportEncoding")
        self.frame_RB_ExportEncoding.setMinimumSize(QSize(4, 0))
        self.frame_RB_ExportEncoding.setMaximumSize(QSize(16777215, 0))
        self.frame_RB_ExportEncoding.setStyleSheet(u"background-color: rgb(37, 38, 44);")
        self.RB_RadioButtons_ExportEncoding = QVBoxLayout(self.frame_RB_ExportEncoding)
        self.RB_RadioButtons_ExportEncoding.setSpacing(2)
        self.RB_RadioButtons_ExportEncoding.setObjectName(u"RB_RadioButtons_ExportEncoding")
        self.radioButton_RB_ExpEnc_system = QRadioButton(self.frame_RB_ExportEncoding)
        self.radioButton_RB_ExpEnc_system.setObjectName(u"radioButton_RB_ExpEnc_system")
        self.radioButton_RB_ExpEnc_system.setStyleSheet(u"")
        self.radioButton_RB_ExpEnc_system.setChecked(True)

        self.RB_RadioButtons_ExportEncoding.addWidget(self.radioButton_RB_ExpEnc_system)

        self.radioButton_RB_ExpEnc_UTF = QRadioButton(self.frame_RB_ExportEncoding)
        self.radioButton_RB_ExpEnc_UTF.setObjectName(u"radioButton_RB_ExpEnc_UTF")
        self.radioButton_RB_ExpEnc_UTF.setStyleSheet(u"")

        self.RB_RadioButtons_ExportEncoding.addWidget(self.radioButton_RB_ExpEnc_UTF)

        self.horizontalLayout_RB_ExpEnc_RadioButtons = QHBoxLayout()
        self.horizontalLayout_RB_ExpEnc_RadioButtons.setSpacing(0)
        self.horizontalLayout_RB_ExpEnc_RadioButtons.setObjectName(u"horizontalLayout_RB_ExpEnc_RadioButtons")
        self.horizontalLayout_RB_ExpEnc_RadioButtons.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.radioButton_RB_ExpEnc_Custom = QRadioButton(self.frame_RB_ExportEncoding)
        self.radioButton_RB_ExpEnc_Custom.setObjectName(u"radioButton_RB_ExpEnc_Custom")
        self.radioButton_RB_ExpEnc_Custom.setMaximumSize(QSize(22, 16777215))
        self.radioButton_RB_ExpEnc_Custom.setStyleSheet(u"")

        self.horizontalLayout_RB_ExpEnc_RadioButtons.addWidget(self.radioButton_RB_ExpEnc_Custom)

        self.lineEdit_RB_ExpEnc_RadioButton_Custom = QLineEdit(self.frame_RB_ExportEncoding)
        self.lineEdit_RB_ExpEnc_RadioButton_Custom.setObjectName(u"lineEdit_RB_ExpEnc_RadioButton_Custom")
        sizePolicy3.setHeightForWidth(self.lineEdit_RB_ExpEnc_RadioButton_Custom.sizePolicy().hasHeightForWidth())
        self.lineEdit_RB_ExpEnc_RadioButton_Custom.setSizePolicy(sizePolicy3)
        self.lineEdit_RB_ExpEnc_RadioButton_Custom.setMinimumSize(QSize(0, 0))
        self.lineEdit_RB_ExpEnc_RadioButton_Custom.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_RB_ExpEnc_RadioButtons.addWidget(self.lineEdit_RB_ExpEnc_RadioButton_Custom)


        self.RB_RadioButtons_ExportEncoding.addLayout(self.horizontalLayout_RB_ExpEnc_RadioButtons)


        self.verticalLayout_13.addWidget(self.frame_RB_ExportEncoding)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.errorLabel = QLabel(self.bottomBar)
        self.errorLabel.setObjectName(u"errorLabel")
        sizePolicy1.setHeightForWidth(self.errorLabel.sizePolicy().hasHeightForWidth())
        self.errorLabel.setSizePolicy(sizePolicy1)
        self.errorLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setItalic(False)
        self.errorLabel.setFont(font4)
        self.errorLabel.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.errorLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.errorLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.version.sizePolicy().hasHeightForWidth())
        self.version.setSizePolicy(sizePolicy6)
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.horizontalLayout_6.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_rG_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"L5X Modifier", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"For RSLogix modification", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Tag to CSV", None))
        self.btn_str_conv.setText(QCoreApplication.translate("MainWindow", u"String converter", None))
        self.btn_rungGenerator.setText(QCoreApplication.translate("MainWindow", u"Rung generator", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save file", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" "
                        "style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"PyDracula APP - Theme with colors based on Dracula for Python.", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.pushButton_tE_OpenFile.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelBox_tE_OpenFile.setText(QCoreApplication.translate("MainWindow", u"Open L5X file", None))
        self.lineEdit_tE_OpenFile.setText("")
        self.lineEdit_tE_OpenFile.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBox_tE_ChooseScope.setText(QCoreApplication.translate("MainWindow", u"Choose tag scope", None))
        self.labelBox_tE_Filter.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.lineEdit_tE_Filter.setText("")
        self.lineEdit_tE_Filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton_tE_Filter.setText("")
        self.labelBox_tE_ChooseTag.setText(QCoreApplication.translate("MainWindow", u"Choose tag name", None))
        self.labelBox_tE_TagTree.setText(QCoreApplication.translate("MainWindow", u"Tag Tree", None))
        self.pushButton_tE_Expand.setText(QCoreApplication.translate("MainWindow", u"Expand", None))
        self.pushButton_tE_Collapse.setText(QCoreApplication.translate("MainWindow", u"Collapse", None))
        self.checkBox_tE_PrintHeaders.setText(QCoreApplication.translate("MainWindow", u"Print headers", None))
        self.checkBox_tE_ConcatenatePath.setText(QCoreApplication.translate("MainWindow", u"Concatenate path", None))
#if QT_CONFIG(tooltip)
        self.radioButton_tE_PL.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Windows-1250</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_tE_PL.setText(QCoreApplication.translate("MainWindow", u"PL", None))
#if QT_CONFIG(tooltip)
        self.radioButton_tE_GFS.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Windows-1252</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_tE_GFS.setText(QCoreApplication.translate("MainWindow", u"GER, FR, SP", None))
#if QT_CONFIG(tooltip)
        self.radioButton_tE_RU.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Windows-1251</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_tE_RU.setText(QCoreApplication.translate("MainWindow", u"RUS, UA", None))
#if QT_CONFIG(tooltip)
        self.radioButton_tE_UTF.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>UTF-8</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_tE_UTF.setText(QCoreApplication.translate("MainWindow", u"UTF-8", None))
#if QT_CONFIG(tooltip)
        self.radioButton_tE_Custom.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>type custom encoder</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_tE_Custom.setText("")
        self.lineEdit_tE_RadioButton_Custom.setText("")
        self.lineEdit_tE_RadioButton_Custom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"other...", None))
        self.pushButton_tE_Export.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.pushButton_tE_Import.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.label_tsC_SimpleText.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.pushButton_tsC_CopyText.setText(QCoreApplication.translate("MainWindow", u"-> Copy Text", None))
        self.pushButton_tsC_PasteText.setText(QCoreApplication.translate("MainWindow", u"<- Paste Text", None))
        self.label_tsC_RSLogixText.setText(QCoreApplication.translate("MainWindow", u"RSLogix String", None))
#if QT_CONFIG(tooltip)
        self.radioButton_tsC_PL.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Windows-1250</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_tsC_PL.setText(QCoreApplication.translate("MainWindow", u"PL", None))
#if QT_CONFIG(tooltip)
        self.radioButton_tsC_GFS.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Windows-1252</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_tsC_GFS.setText(QCoreApplication.translate("MainWindow", u"GER, FR, SP", None))
#if QT_CONFIG(tooltip)
        self.radioButton_tsC_RU.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Windows-1251</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_tsC_RU.setText(QCoreApplication.translate("MainWindow", u"RUS, UA", None))
#if QT_CONFIG(tooltip)
        self.radioButton_tsC_UTF.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>UTF-8</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_tsC_UTF.setText(QCoreApplication.translate("MainWindow", u"UTF-8", None))
#if QT_CONFIG(tooltip)
        self.radioButton_tsC_Custom.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>type custom encoder</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_tsC_Custom.setText("")
        self.lineEdit_tsC_RadioButton_Custom.setText("")
        self.lineEdit_tsC_RadioButton_Custom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"other...", None))
        self.pushButton_tsC_CopyRSL.setText(QCoreApplication.translate("MainWindow", u"-> Copy RSL", None))
        self.pushButton_tsC_PasteRSL.setText(QCoreApplication.translate("MainWindow", u"<- Paste RSL", None))
        self.lineEdit_rG_config_OpenFile.setText("")
        self.lineEdit_rG_config_OpenFile.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton_rG_config_OpenFile.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelBox_rG_config_OpenFile.setText(QCoreApplication.translate("MainWindow", u"Configuration file", None))
        self.pushButton_rG_preparePage.setText(QCoreApplication.translate("MainWindow", u"Prepare CSV file", None))
        self.pushButton_rG_importPage.setText(QCoreApplication.translate("MainWindow", u"Import CSV file", None))
        self.lineEdit_rG_rungs_OpenFile.setText("")
        self.lineEdit_rG_rungs_OpenFile.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton_rG_rungs_OpenFile.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelBox_rG_rungs_OpenFile.setText(QCoreApplication.translate("MainWindow", u"Rungs Template", None))
        self.lineEdit_rG_fault_OpenFile.setText("")
        self.lineEdit_rG_fault_OpenFile.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBox_rG_fault_OpenFile.setText(QCoreApplication.translate("MainWindow", u"Fault Template", None))
        self.pushButton_rG_fault_OpenFile.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.pushButton_rG_saveConfiguration.setText(QCoreApplication.translate("MainWindow", u"Save configuration file", None))
        self.pushButton_rG_exportCSV.setText(QCoreApplication.translate("MainWindow", u"export tag CSV file", None))
        self.labelBox_rG_treeHeader.setText(QCoreApplication.translate("MainWindow", u"Rungs Template", None))
        self.pushButton_rG_appear.setText(QCoreApplication.translate("MainWindow", u"appear order", None))
        self.pushButton_rG_alphabetical.setText(QCoreApplication.translate("MainWindow", u"alphabetical", None))
        self.labelBox_rG_chooseProgram.setText(QCoreApplication.translate("MainWindow", u"Choose Program", None))
        self.labelBox_rG_chooseRungsRoutine.setText(QCoreApplication.translate("MainWindow", u"Choose Rungs Routine", None))
        self.labelBox_rG_rungs_rungNumber.setText(QCoreApplication.translate("MainWindow", u"rung number (-1)", None))
        self.lineEdit_rG_rungs_rungNumber.setText("")
        self.lineEdit_rG_rungs_rungNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"other...", None))
        self.labelBox_rG_chooseFaultsRoutine.setText(QCoreApplication.translate("MainWindow", u"Choose faults routine", None))
        self.labelBox_rG_faults_rungNumber.setText(QCoreApplication.translate("MainWindow", u"rung number (-1)", None))
        self.lineEdit_rG_faults_rungNumber.setText("")
        self.lineEdit_rG_faults_rungNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"other...", None))
        self.pushButton_rG_generateInProject.setText(QCoreApplication.translate("MainWindow", u"Generate in project", None))
        self.pushButton_rG_generateExportFiles.setText(QCoreApplication.translate("MainWindow", u"Generate in export files", None))
        self.pushButton_RB_ExportEncoding.setText(QCoreApplication.translate("MainWindow", u"Export encoding", None))
#if QT_CONFIG(tooltip)
        self.radioButton_RB_ExpEnc_system.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Encoding set by system</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_RB_ExpEnc_system.setText(QCoreApplication.translate("MainWindow", u"System encoding", None))
#if QT_CONFIG(tooltip)
        self.radioButton_RB_ExpEnc_UTF.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>UTF-8</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_RB_ExpEnc_UTF.setText(QCoreApplication.translate("MainWindow", u"UTF-8", None))
#if QT_CONFIG(tooltip)
        self.radioButton_RB_ExpEnc_Custom.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>type custom encoder</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_RB_ExpEnc_Custom.setText("")
        self.lineEdit_RB_ExpEnc_RadioButton_Custom.setText("")
        self.lineEdit_RB_ExpEnc_RadioButton_Custom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"other...", None))
        self.errorLabel.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.1.0", None))
    # retranslateUi

