import RPi.GPIO as GPIO


class Convertor:
    def _init_(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)
        GPIO.setup(21, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(26, GPIO.OUT)

    # Convert unrecognizable character into Unrecognizable(R).
    def filterUnrecognizable(self, c):
        if not self.isConvertable(c):
            c = '{'
        return c

    # Check if a character is convertable.
    def isConvertable(self, a):
        return a in dict

    # Convert a letter to a list of binary commands.
    def convertor(self, a):
        return dict.get(a)

    # Change an array of binary Braille dot commands to actual output commands.
    # GPIO 16 for left-upper; GPIO 20 for left-middle; GPIO 21 for left-down;
    # GPIO 13 for right-upper; GPIO 19 for right-middle; GPIO 26 for right-down.
    def output(self, booleanValues):
        high = list()
        low = list()

        if booleanValues[0] == 1:
            high.append(16)
        else:
            low.append(16)

        if booleanValues[1] == 1:
            high.append(20)
        else:
            low.append(20)

        if booleanValues[2] == 1:
            high.append(21)
        else:
            low.append(21)

        if booleanValues[3] == 1:
            high.append(13)
        else:
            low.append(13)

        if booleanValues[4] == 1:
            high.append(19)
        else:
            low.append(19)

        if booleanValues[5] == 1:
            high.append(26)
        else:
            low.append(26)

        GPIO.output(high, 1)
        GPIO.output(low, 0)

        