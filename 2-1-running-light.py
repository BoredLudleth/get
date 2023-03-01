import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

chan_list = [21, 20, 16, 12, 7, 8, 25, 24] 
GPIO.setup(chan_list, GPIO.OUT)

for i in range (0,3):
    for j in chan_list:
        GPIO.output (j, 1)
        time.sleep(0.2)
        GPIO.output (chan_list, 0)

GPIO.cleanup()