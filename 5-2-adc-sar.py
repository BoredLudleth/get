import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup (dac, GPIO.OUT)
GPIO.setup (troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)

def decimal2binary (value):
    return [int (element) for element in bin (value)[2:].zfill(8)]

def binary2list(array, value):
    for i in range (0, 8):
        if (value & pow(2, i) == pow(2, i)):
            array[7 - i] = 1
        else:
            array[7 - i] = 0
    return array

def adc(array):
    result = 0
    for i in range  (7, -1, -1):
        result += 2 ** i
        decimal2binary(result)
        binary2list(array, result)
        GPIO.output (dac, array)
        if (GPIO.input(comp) == 0):
            result -= 2 ** i
        time.sleep (0.5)
    print(3.3 * result / 255)
    return

array = [0, 0, 0, 0, 0, 0, 0, 0]

command = 1

while (command):
    try:
        while (1):
            adc (array)

    finally:
        GPIO.output (dac, [0,0,0,0,0,0,0,0])
        GPIO.cleanup()
        command = 0