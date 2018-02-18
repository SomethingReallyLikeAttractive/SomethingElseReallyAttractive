from Loader import FileLoader
from Convertor import ENGLISH
import RPi.GPIO as GPIO

BUTTONPIN = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTONPIN, GPIO.IN)

detectedLoader = FileLoader("SampleText.txt")
print("The following word is detected")
print(detectedLoader.returnText())
detectedLoader.sendTextToRasp()

GPIO.output([14, 18, 23, 25, 7, 12], 0)
GPIO.cleanup()