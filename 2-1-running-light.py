import time
import RPi.GPIO as GPIO

leds = [2, 3, 4, 17, 27,22, 18, 9]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

for i in range(3):
    for elem in leds:
        GPIO.output(elem, 1)
        time.sleep(0.2)
        GPIO.output(elem, 0)

GPIO.output(leds, 0)
GPIO.cleanup()