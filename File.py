from Convertor import Convertor

class File:
    _fileText = None

    def _init_(self):
        fileOpened = open("text.txt", "r")
        self._fileText = fileOpened.read()

    def sendFileToRasp(self):
        fileConvertor = Convertor()
        for c in self._fileText:
            a = fileConvertor.filterUnrecognizable(c)
            fileConvertor.output(fileConvertor.convertor(a))