from PySide6.QtGui import QGuiApplication
from main import MainWindow
import warnings


class StringConverter(MainWindow):

    def __init__(self, widgets, L5XMod):
        # COPIED FROM PARENT
        self.widgets = widgets
        self.L5XMod = L5XMod

        # SUBCLASS PARAMETERS
        self.clipboard = QGuiApplication.clipboard()

        # SIGNALS AND SLOTS CONNECTIONS
        self.widgets.lineEdit_tsC_RadioButton_Custom.editingFinished.connect(self.radioButtons_custom_check)
        self.widgets.radioButton_tsC_PL.clicked.connect(self.simpleText_translate)
        self.widgets.radioButton_tsC_GFS.clicked.connect(self.simpleText_translate)
        self.widgets.radioButton_tsC_RU.clicked.connect(self.simpleText_translate)
        self.widgets.radioButton_tsC_UTF.clicked.connect(self.simpleText_translate)
        self.widgets.textEdit_tsC_SimpleText.textChanged.connect(self.simpleText_translate)
        self.widgets.textEdit_tsC_RSLogixText.textChanged.connect(self.RSLText_edited)
        self.widgets.pushButton_tsC_CopyText.clicked.connect(self.CopyTest_clicked)
        self.widgets.pushButton_tsC_CopyRSL.clicked.connect(self.CopyRSL_clicked)
        self.widgets.pushButton_tsC_PasteText.clicked.connect(self.PasteText_clicked)
        self.widgets.pushButton_tsC_PasteRSL.clicked.connect(self.PasteRSL_clicked)

    def radioButtons_get_encoder(self):
        radioButtons = {self.widgets.radioButton_tsC_PL: "Windows-1250",
                        self.widgets.radioButton_tsC_GFS: "Windows-1252",
                        self.widgets.radioButton_tsC_RU: "Windows-1251",
                        self.widgets.radioButton_tsC_UTF: "UTF-8"}
        for item in radioButtons:
            if item.isChecked():
                return radioButtons[item]
        if self.widgets.radioButton_tsC_Custom.isChecked()\
                and self.widgets.lineEdit_tsC_RadioButton_Custom.text() != "":
            return self.widgets.lineEdit_tsC_RadioButton_Custom.text().lower()
        else:
            return None

    def radioButtons_custom_check(self):
        if not self.L5XMod.check_custom_ecnoder(self.widgets.lineEdit_tsC_RadioButton_Custom.text()):
            self.widgets.lineEdit_tsC_RadioButton_Custom.clear()
        elif self.widgets.radioButton_tsC_Custom.isChecked():
            self.simpleText_translate()

    def simpleText_translate(self):
        self.clear_error()
        string = self.widgets.textEdit_tsC_SimpleText.toPlainText()
        encoder = self.radioButtons_get_encoder()
        self.widgets.textEdit_tsC_RSLogixText.blockSignals(True)
        with warnings.catch_warnings(record=True) as w:
            self.widgets.textEdit_tsC_RSLogixText.setPlainText(self.L5XMod.encode_string(string, encoder))
            if w:
                print("Warning: " + str(w[-1]))
                self.display_error(str(w[-1].message))
        self.widgets.textEdit_tsC_RSLogixText.blockSignals(False)

    def RSLText_edited(self):
        self.clear_error()
        string = self.widgets.textEdit_tsC_RSLogixText.toPlainText()
        encoder = self.radioButtons_get_encoder()
        self.widgets.textEdit_tsC_SimpleText.blockSignals(True)
        self.widgets.textEdit_tsC_SimpleText.setPlainText(self.L5XMod.decode_string(string, encoder))
        self.widgets.textEdit_tsC_SimpleText.blockSignals(False)

    def CopyTest_clicked(self):
        self.clear_error()
        self.clipboard.setText(self.widgets.textEdit_tsC_SimpleText.toPlainText())

    def CopyRSL_clicked(self):
        self.clear_error()
        self.clipboard.setText(self.widgets.textEdit_tsC_RSLogixText.toPlainText())

    def PasteText_clicked(self):
        self.clear_error()
        self.widgets.textEdit_tsC_SimpleText.setPlainText(self.clipboard.text())

    def PasteRSL_clicked(self):
        self.clear_error()
        self.widgets.textEdit_tsC_RSLogixText.setPlainText(self.clipboard.text())
