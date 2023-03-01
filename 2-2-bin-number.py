import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0,0,0,0,0,1,0,1]

GPIO.setup(dac, GPIO.OUT)

GPIO.output (dac, number)
time.sleep(15)
GPIO.output (dac, 0)

GPIO.cleanup()

# 255 - 11111111 - 3.26 можно считать максимум малинки
# 127 - 01111111 - 1.63
# 64  - 01000000 - 0.82
# 32  - 00100000 - 0.5
# 5   - 00000101 - 0.48
# 0   - 00000000 - 0.485
# 256 - 10000000 - 9-ти разрядное число реакция как-будто все нули
