import RPi.GPIO as GPIO

pin1 = 14
pin2 = 18
pin3 = 23
pin4 = 25
pin5 = 7
pin6 = 3

class Convertor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        GPIO.setup(pin3, GPIO.OUT)
        GPIO.setup(pin4, GPIO.OUT)
        GPIO.setup(pin5, GPIO.OUT)
        GPIO.setup(pin6, GPIO.OUT)

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
            high.append(pin1)
        else:
            low.append(pin1)

        if booleanValues[1] == 1:
            high.append(pin2)
        else:
            low.append(pin2)

        if booleanValues[2] == 1:
            high.append(pin3)
        else:
            low.append(pin3)

        if booleanValues[3] == 1:
            high.append(pin4)
        else:
            low.append(pin4)

        if booleanValues[4] == 1:
            high.append(pin5)
        else:
            low.append(pin5)

        if booleanValues[5] == 1:
            high.append(pin6)
        else:
            low.append(pin6)

        for c in high:
            print(c)
        print("----")
        for c in low:
            print(c)
        #GPIO.output(high, 1)
        #GPIO.output(low, 0)


dict = {'A':[1,0,0,0,0,0],
        'B':[1,1,0,0,0,0],
        'C':[1,0,0,1,0,0],
        'D':[1,0,0,1,1,0],
        'E':[1,0,0,0,1,0],
        'F':[1,1,0,1,0,0],
        'G':[1,1,0,1,1,0],
        'H':[1,1,0,0,1,0],
        'I':[0,1,0,1,0,0],
        'J':[0,1,0,1,1,0],
        'K':[1,0,1,0,0,0],
        'L':[1,1,1,0,0,0],
        'M':[1,0,1,1,0,0],
        'N':[1,0,1,1,1,0],
        'O':[1,0,1,0,1,0],
        'P':[1,1,1,1,0,0],
        'Q':[1,1,1,1,1,0],
        'R':[1,1,1,0,1,0],
        'S':[0,1,1,1,0,0],
        'T':[0,1,1,1,1,0],
        'U':[1,0,1,0,0,1],
        'V':[1,1,1,0,0,1],
        'W':[0,1,0,1,1,1],
        'X':[1,0,1,1,0,1],
        'Y':[1,0,1,1,1,1],
        'Z':[1,0,1,0,1,1],
        '#':[0,0,1,1,1,1],
        '0':[0,1,0,1,1,0],
        '1':[1,0,0,0,0,0],
        '2':[1,1,0,0,0,0],
        '3':[1,0,0,1,0,0],
        '4':[1,0,0,1,1,0],
        '5':[1,0,0,0,1,0],
        '6':[1,1,0,1,0,0],
        '7':[1,1,0,1,1,0],
        '8':[1,1,0,0,1,0],
        '9':[0,1,0,1,0,0],
        '.':[0,1,0,0,1,1],
        ',':[0,1,0,0,0,0],
        '!':[0,1,1,0,1,0],
        '?':[0,1,1,0,0,1],
        ':':[0,1,0,0,1,0],
        ';':[0,1,1,0,0,0],
        '-':[0,0,1,0,0,1],
        '(':[0,1,1,0,1,1],
        ')':[0,1,1,0,1,1],
        '<':[1,1,0,0,0,1],
        '>':[0,0,1,1,1,0],
        '/':[0,0,1,1,0,0],
        '"':[0,1,1,0,0,1],
        '\'':[0,0,1,0,0,0],
        }
