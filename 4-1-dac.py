import RPi.GPIO as GPIO

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
        while (1):
            value = int(input())

            if (value == 'q'):
                break

            if (value > 255 or value < 0):
                print('Не хватает разрядности.. Добавляю.. 0шИбКа...')
                break

            binary2list (array, value)
            GPIO.output (dac, array)
            print ("U = ", (value/pow(2, 8) * 3.3))
            
    except ValueError:
        print('Это не число. Выходим.')

    finally:
        GPIO.output (dac, [0,0,0,0,0,0,0,0])
        GPIO.cleanup()
        command = 0
