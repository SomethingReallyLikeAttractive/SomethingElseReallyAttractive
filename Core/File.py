from Convertor import Convertor

class File:
    _fileText = None

    def __init__(self, fileName):
        fileOpened = open(fileName, "r")
        self._fileText = fileOpened.read()

    def sendFileToRasp(self):
        fileConvertor = Convertor()
        for c in self._fileText:
            a = fileConvertor.filterUnrecognizable(c)
            fileConvertor.output(fileConvertor.convertor(a))
