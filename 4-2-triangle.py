import RPi.GPIO as GPIO
import time

def decimal2binary (value):
    return [int (element) for element in bin (value)[2:].zfill(8)]

def binary2list(array, value):
    for i in range (0, 8):
        if (value & pow(2, i) == pow(2, i)):
            array[7 - i] = 1
        else:
            array[7 - i] = 0
    return array

GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
array = [0, 0, 0, 0, 0, 0, 0, 0]
GPIO.setup (dac, GPIO.OUT)

command = 1

while (command):
    try:
        per = float(input())
        per = per / 512
        value = 0
        while (1):
            while (value < 255):
                value = value + 1
                time.sleep (per)
                binary2list (array, value)
                GPIO.output (dac, array)
                print(array)
            while (value > 0):
                value = value - 1
                time.sleep (per)
                binary2list (array, value)
                GPIO.output (dac, array)
                print (array)
            
    except ValueError:
        print('Это не число. Выходим.')

    finally:
        GPIO.output (dac, [0,0,0,0,0,0,0,0])
        GPIO.cleanup()
        command = 0
