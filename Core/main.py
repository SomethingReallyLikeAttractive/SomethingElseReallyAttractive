from Loader import FileLoader
from Convertor import ENGLISH
import RPi.GPIO as GPIO
import time
import subprocess

BUTTONPIN = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTONPIN, GPIO.IN)

while True:
    if (GPIO.input() == True):

    time.sleep(0.05)