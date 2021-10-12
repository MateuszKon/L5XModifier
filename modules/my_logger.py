class MyLogger(object):

    def __init__(self, original, file):
        self.original = original
        self.f = open(file, 'w')

    def write(self, obj):
        self.f.write(obj)
        self.original.write(obj)
        self.flush()

    def close(self):
        self.f.close()

    def flush(self):
        self.f.flush()
        self.original.flush()
