from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QTimer
import sys

class StatusBar:

    def __init__(self, status_bar_widget: QLabel):
        self.widget = status_bar_widget
        self.timer: QTimer = self.init_timer()
        self.default = True

    def __enter__(self):
        self.display_warning("In progress", False)
        self.default = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.display_info("Done", True)
            self.default = True
        elif self.default:
            self.display_error(str(exc_val))
            # sys.excepthook(exc_type, exc_val, exc_tb)

    def init_timer(self) -> QTimer:
        timer = QTimer()
        timer.setInterval(5000)
        timer.setSingleShot(True)
        timer.timeout.connect(self.clear_error)
        return timer

    def display_error(self, message, start_timer=False):
        self.display(message, "red", start_timer)

    def display_warning(self, message, start_timer=False):
        self.display(message, "yellow", start_timer)

    def display_info(self, message, start_timer=False):
        self.display(message, "green", start_timer)

    def display(self, message, color, start_timer=False):
        self.widget.setStyleSheet("color: {}".format(color))
        self.widget.setText(message)
        self.default = False
        if start_timer:
            self.timer.start()

    def clear_error(self):
        self.widget.clear()
        self.default = True
