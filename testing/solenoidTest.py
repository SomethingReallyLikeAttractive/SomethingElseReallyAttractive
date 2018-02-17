import RPi.GPIO as GPIO

testPin = 7
testPin2 = 8
state = input("On (1) or Off (2)?")


GPIO.setmode(GPIO.BCM)
GPIO.setup(testPin, GPIO.OUT)

GPIO.output(testPin, GPIO.LOW)

try:
	while 1:
		if state == 1:
			GPIO.output(testPin, GPIO.HIGH)

		if state == 2:
			GPIO.output(testPin, GPIO.LOW)
		
except KeyboardInterrupt:
	GPIO.output(testPin, GPIO.LOW)
	GPIO.cleanup()