from Convertor import Convertor
import time

class Loader:
    text = ""

    def sendTextToRasp(self):
        convertor = Convertor()
        for c in self.text:
            a = convertor.processString(c)
            convertor.output(convertor.convert(a))
            time.sleep(1)

    def returnText(self):
        return self.text

class FileLoader(Loader):
    def __init__(self, fileName):
        fileOpened = open(fileName, "r")
        self.text = fileOpened.read()

class StringLoader(Loader):
    def __init__(self, string):
        self.text = string