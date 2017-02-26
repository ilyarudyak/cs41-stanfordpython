from io import StringIO
import sys


class Silencer():
    def __init__(self):
        self.mystdout = StringIO()

    def __enter__(self):
        sys.stdout = self.mystdout

    def __exit__(self, *exc):
        sys.stdout = sys.__stdout__

    def __str__(self):
        return self.mystdout.getvalue()