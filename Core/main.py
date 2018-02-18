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
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTONPIN,GPIO.IN)

    input()
    result = subprocess.check_output('ls')
    #result = subprocess.check_output('fswebcam -r 4352x3264 --no-banner img.jpg && tesseract img.jpg Picwords.txt')
    #wordDetected = result.decode("utf-8")
    detectedLoader = StringLoader(result)
    detectedLoader.sendTextToRasp()
    time.sleep(0.05)
