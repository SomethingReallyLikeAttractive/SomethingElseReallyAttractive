import RPi.GPIO as GPIO

pin1 = 14
pin2 = 18
pin3 = 23
pin4 = 25
pin5 = 7
pin6 = 3

englishDict = setUpDict()

def setUpDict():
    englishDict = dict()
    englishDict['A'] = [1,0,0,0,0,0]
    englishDict['B'] = [1,1,0,0,0,0]
    englishDict['C'] = [1,0,0,1,0,0]
    englishDict['D'] = [1,0,0,1,1,0]
    englishDict['E'] = [1,0,0,0,1,0]
    englishDict['F'] = [1,1,0,1,0,0]
    englishDict['G'] = [1,1,0,1,1,0]
    englishDict['H'] = [1,1,0,0,1,0]
    englishDict['I'] = [0,1,0,1,0,0]
    englishDict['J'] = [0,1,0,1,1,0]
    englishDict['K'] = [1,0,1,0,0,0]
    englishDict['L'] = [1,1,1,0,0,0]
    englishDict['M'] = [1,0,1,1,0,0]
    englishDict['N'] = [1,0,1,1,1,0]
    englishDict['O'] = [1,0,1,0,1,0]
    englishDict['P'] = [1,1,1,1,0,0]
    englishDict['Q'] = [1,1,1,1,1,0]
    englishDict['R'] = [1,1,1,0,1,0]
    englishDict['S'] = [0,1,1,1,0,0]
    englishDict['T'] = [0,1,1,1,1,0]
    englishDict['U'] = [1,0,1,0,0,1]
    englishDict['V'] = [1,1,1,0,0,1]
    englishDict['W'] = [0,1,0,1,1,1]
    englishDict['X'] = [1,0,1,1,0,1]
    englishDict['Y'] = [1,0,1,1,1,1]
    englishDict['Z'] = [1,0,1,0,1,1]
    englishDict['#'] = [0,0,1,1,1,1]
    englishDict['0'] = [0,1,0,1,1,0]
    englishDict['1'] = [1,0,0,0,0,0]
    englishDict['2'] = [1,1,0,0,0,0]
    englishDict['3'] = [1,0,0,1,0,0]
    englishDict['4'] = [1,0,0,1,1,0]
    englishDict['5'] = [1,0,0,0,1,0]
    englishDict['6'] = [1,1,0,1,0,0]
    englishDict['7'] = [1,1,0,1,1,0]
    englishDict['8'] = [1,1,0,0,1,0]
    englishDict['9'] = [0,1,0,1,0,0]
    englishDict['.'] = [0,1,0,0,1,1]
    englishDict[','] = [0,1,0,0,0,0]
    englishDict['!'] = [0,1,1,0,1,0]
    englishDict['?'] = [0,1,1,0,0,1]
    englishDict[':'] = [0,1,0,0,1,0]
    englishDict[';'] = [0,1,1,0,0,0]
    englishDict['-'] = [0,0,1,0,0,1]
    englishDict['('] = [0,1,1,0,1,1]
    englishDict[')'] = [0,1,1,0,1,1]
    englishDict['<'] = [1,1,0,0,0,1]
    englishDict['>'] = [0,0,1,1,1,0]
    englishDict['/'] = [0,0,1,1,0,0]
    englishDict['"'] = [0,1,1,0,0,1]
    englishDict['\\'] = [0,0,1,0,0,0]
    return englishDict

class Convertor:
    def __init__(self):
        setUpDict()
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
            c = englishDict['{']
        return c

    # Check if a character is convertable.
    def isConvertable(self, a):
        return a in englishDict

    # Convert a letter to a list of binary commands.
    def convertor(self, a):
        return englishDict[a]

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
        GPIO.cleanup()