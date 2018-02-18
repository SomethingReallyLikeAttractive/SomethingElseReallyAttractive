from Loader import FileLoader, StringLoader
from Convertor import ENGLISH
import RPi.GPIO as GPIO
import time
#import subprocess
import os

BUTTONPIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTONPIN, GPIO.IN)

while True:
    os.system('fswebcam -r 4352x3264 --no-banner img.jpg && tesseract img.jpg Picwords')
    detectedLoader = FileLoader("Picwords.txt")
    print("The following word is detected: ")
    print(detectedLoader.returnText())
    detectedLoader.sendTextToRasp()
    time.sleep(0.05)

GPIO.output([14, 18, 23, 25, 7, 12], 0)
os.system('rm Picwords.txt')
GPIO.cleanup()