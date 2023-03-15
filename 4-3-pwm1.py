import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)

GPIO.setup (22, GPIO.OUT)

command = 1
dutycycle = 1

while (command):
    try:
        p = GPIO.PWM (22, 50)
        while(1): 
            p.start(dutycycle)
            dutycycle = int(input())


    finally:
        GPIO.output (22, 0)
        GPIO.cleanup()
        command = 0