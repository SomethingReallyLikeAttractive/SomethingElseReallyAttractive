from Convertor import Convertor
import time
import requests

class Loader:
    text = ""

    def sendTextToRasp(self):
        convertor = Convertor()
        for c in self.text:
            a = convertor.processString(c)
            convertor.output(convertor.convert(a))
            #r = requests.post('http://0.0.0.0:5000',data=a)
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
