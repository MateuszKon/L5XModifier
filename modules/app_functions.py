from main import MainWindow
from .app_settings import Settings


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
