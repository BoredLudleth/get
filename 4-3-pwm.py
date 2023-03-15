import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)

GPIO.setup (24, GPIO.OUT)
GPIO.setup (25, GPIO.OUT, initial = 1)

command = 1
dutycycle = 1

while (command):
    try:
        while(1): 
            p = GPIO.PWM (24, 50)
            p.start(dutycycle)
            dutycycle = int(input())
            p.stop ()

    finally:
        GPIO.output (24, 0)
        GPIO.cleanup()
        command = 0
