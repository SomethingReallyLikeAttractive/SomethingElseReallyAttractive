from Loader import FileLoader
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
loadFile = FileLoader("Text.txt")
loadFile.sendTextToRasp()