from Loader import FileLoader, StringLoader
from Convertor import ENGLISH
import RPi.GPIO as GPIO
import time
import subprocess

BUTTONPIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTONPIN, GPIO.IN)

fileLoader = FileLoader('Text.txt')
fileLoader.sendTextToRasp()

while True:
    if (GPIO.input() == True):
        result = subprocess.run('fswebcam -r 4352x3264 --no-banner img.jpg && tesseract img.jpg stdout', stdout = subprocess.PIPE)
        wordDetected = result.stdout.read()
        detectedLoader = StringLoader(wordDetected)
        detectedLoader.sendTextToRasp()
    time.sleep(0.05)