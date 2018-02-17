from Loader import FileLoader
from Convertor import ENGLISH
from time import time


dateLastOpened = 0
dateFile = open("DateLastOpened.txt", "r+")
dateLastOpened = int(dateFile.read())
dateFile.write(time())

# Test code
b = FileLoader("Text.txt")
b.sendTextToRasp()


