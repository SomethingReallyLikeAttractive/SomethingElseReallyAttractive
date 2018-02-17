from Loader import FileLoader
from Convertor import ENGLISH
import time


dateLastOpened = 0
dateFile = open("DateLastOpened.txt", "r+")
dateLastOpened = int(dateFile.read())
dateFile.write(time.time())

# Test code
b = FileLoader("Text.txt")
b.sendTextToRasp()
