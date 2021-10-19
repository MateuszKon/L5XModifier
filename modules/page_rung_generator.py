from main import MainWindow
from PySide6.QtWidgets import QFileDialog


class RungGeneratorPage(MainWindow):

    def __init__(self, widgets):
        self.widgets = widgets
        self.current_rung_file = ""

        # CONNECT SIGNALS TO SLOTS
        widgets.pushButton_rG_rungs_OpenFile.clicked.connect(self.rungs_openFile_button)

    def rungs_openFile_button(self):
        dialog = QFileDialog()
        dialog.setNameFilters(["RSLogix exported rungs L5X files (*.L5X)"])
        if dialog.exec():
            self.widgets.lineEdit_rG_rungs_OpenFile.setText(dialog.selectedFiles()[0])
            self.current_rung_file = dialog.selectedFiles()[0]
            self.rungs_file_changed()
        else:
            self.widgets.lineEdit_rG_rungs_OpenFile.setText(self.current_rung_file)

    def rungs_file_changed(self):
        pass