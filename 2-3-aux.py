import time
import RPi.GPIO as GPIO

leds = [2, 3, 4, 17, 27,22, 18, 9]
aux=[21,20,26,16,19,25,23,24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)
GPIO.output(leds, 0)
rng = [0,1,2,3,4,5,6,7]

while True:
    for i in rng:
        GPIO.output(leds[i],GPIO.input(aux[i]))
        time.sleep(0.5)
        #GPIO.output(leds[i], 0)

GPIO.output(leds, 0)
GPIO.cleanup()