import RPi.GPIO as GPIO
from time import sleep
import matplotlib.pyplot as plt
import numpy as np

GPIO.setmode (GPIO.BCM)

leds = [21,20, 16, 12, 7, 8, 25, 24]

dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4

troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.OUT)

def getTroykaU ():
    return GPIO.input(troyka)

array = [0, 0, 0, 0, 0, 0, 0, 0]

def decimal2binary (value):
    return [int (element) for element in bin (value)[2:].zfill(8)]

def binary2list(array, value):
    for i in range (0, 8):
        if (value & pow(2, i) == pow(2, i)):
            array[7 - i] = 1
        else:
            array[7 - i] = 0
    return array

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        GPIO.output(dac, decimal2binary(k))
        sleep(0.005)
        if GPIO.input(comp)==0:
            k-=2**i
    return k

f = open("data.txt", 'w')

f2 = open("setting.txt", 'w')

try:
    step = 0.05

    data = []
    i = 0
    current_data = 0
    
    GPIO.output (troyka, 0)
    sleep (3)
    GPIO.output (troyka, 1)

    while (current_data < 0.65):
        current_data = adc() * 3.3 / 255
        data.append(current_data)
        print(current_data)
        sleep(step)
        i += 1

    GPIO.output (troyka, 0)
    GPIO.output (dac, [0,0,0,0,0,0,0,0])

    while (current_data > 0.2):
        current_data = adc() * 3.3 / 255
        data.append(current_data)
        print(current_data)
        sleep(step)
        i += 1

    for j in data:
        f.write(str(j)+'\n')


    f2.write('Шаг '+str(step)+'\n')
    f2.write('Частота дикретизации '+str(3.3/256)+'\n')
    x = np.arange(0, 101, 1)
    plt.plot(data)
    plt.show()

    print ("step = ", step)
    print ("sampling frequency = ", 1/step)
    



except KeyboardInterrupt:
        print ("KeyboardInterrupt")
finally:
    GPIO.output (dac, [0,0,0,0,0,0,0,0])
    GPIO.cleanup()
    command = 0