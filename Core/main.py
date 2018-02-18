from Loader import FileLoader, StringLoader
from Convertor import ENGLISH
import RPi.GPIO as GPIO
import time
import os
from Display import Display


BUTTONPIN = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTONPIN, GPIO.IN)

#display = Display()

try:
    while True:
        os.system('fswebcam -r 4352x3264 --no-banner img.jpg && tesseract img.jpg Picwords')
        detectedLoader = FileLoader("Picwords.txt")
        print("The following word is detected: ")
        print(detectedLoader.returnText())
        #display.updateText(detectedLoader.returnText())
        detectedLoader.sendTextToRasp()
except KeyboardInterrupt:
    pass

GPIO.output([14, 18, 23, 25, 7, 12], 0)
os.system('rm Picwords.txt')
os.system('rm img.jpg')
GPIO.cleanup()