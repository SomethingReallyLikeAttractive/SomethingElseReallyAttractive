import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12. GPIO.OUT)

# Break a string into characters. Convert unrecognizable character into Unrecognizable(R).
def parser(incomingString):
    for c in incomingString:
        if not isConvertable(c):
            c = '{'

    return c

# Check if a character is convertable.
def isConvertable(a):
    return a in dict

# Convert a letter to a list of binary commands.
def convertor(a):
    return dict.get(a)
#54, 56, 41, 77, 58, 59,

# Change an array of binary Braille dot commands to actual output commands.
# GPIO 16 for left-upper; GPIO 20 for left-middle; GPIO 21 for left-down;
# GPIO 13 for right-upper; GPIO 19 for right-middle; GPIO 26 for right-down.
def output(booleanValues):
    high = list()
    low = list()

    if booleanValues[0] == 1
        high.append(16)
    else
        low.append(16)

    if booleanValues[1] == 1
        high.append(20)
    else
        low.append(20)

    if booleanValues[2] == 1
        high.append(21)
    else
        low.append(21)

    if booleanValues[3] == 1
        high.append(13)
    else
        low.append(13)

    if booleanValues[4] == 1
        high.append(19)
    else
        low.append(19)

    if booleanValues[5] == 1
        high.append(26)
    else
        low.append(26)

    GPIO.output(high, 1)
    GPIO.output(low, 0)

