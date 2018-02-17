class File:
    fileOpened = None

    def _init_(self):
        self.fileOpened = open("text.txt", "r")

    def readFile(self):
        return self.fileOpened.read()