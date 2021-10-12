from modules import *


class MyDialog(QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.ui = Ui_MyDialog()
        self.ui.setupUi(self)
        self.ui.OK_PB.setDefault(True)

        # Signals and Slots
        self.ui.OK_PB.clicked.connect(self.accept)
        self.ui.Cancel_PB.clicked.connect(self.reject)
        self.ui.closeAppBtn.clicked.connect(self.reject)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

        # MOVE WINDOW / MAXIMIZE / RESTORE
        def moveWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                p = event.globalPosition()
                globalPos = p.toPoint()
                self.move(self.pos() + globalPos - self.dragPos)
                self.dragPos = globalPos
                event.accept()
        self.ui.header.mouseMoveEvent = moveWindow

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos

        # def moveWindow(event):
        #     # # IF MAXIMIZED CHANGE TO NORMAL
        #     # if UIFunctions.returStatus(self):
        #     #     UIFunctions.maximize_restore(self)
        #     # MOVE WINDOW
        #     if event.buttons() == Qt.LeftButton:
        #         self.move(self.pos() + event.globalPos() - self.dragPos)
        #         self.dragPos = event.globalPos()
        #         event.accept()
        #
        # self.ui.header.mouseMoveEvent = moveWindow


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = MyDialog()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())

