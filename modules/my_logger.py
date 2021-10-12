import sys
import traceback
from datetime import datetime


class MyLogger(object):

    def __init__(self, original_stdout, original_excepthook, file):
        self.original_stdout = original_stdout
        self.original_excepthook = original_excepthook
        self.f = open(file, 'w')

    def exception_handler(self, exc_type, exc_value, exc_traceback):
        # exc_string = "Unhandled Error\nType: {}\nValue: {}\nTraceback: {}".format(exc_type, exc_value, exc_traceback)
        header_string = "Unhandled Error " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + "\n"
        exc_string = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback)) + "\n"
        self.f.write(header_string + exc_string)
        self.original_excepthook(exc_type, exc_value, exc_traceback)
        self.flush()

    def write(self, obj):
        header_string = "Log " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + "\n"
        self.f.write(header_string)
        self.f.write(obj)
        self.original_stdout.write(obj)
        self.flush()

    def close(self):
        self.f.close()

    def flush(self):
        self.f.flush()
        self.original_stdout.flush()
