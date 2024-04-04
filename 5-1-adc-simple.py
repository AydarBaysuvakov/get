import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def adc():
    for i in range(255):
        GPIO.output(dac, decimal2binary(i))
        if GPIO.input(comp):
            return i
        time.sleep(0.005)
    return 0
        

try:
    while True:
        digit = adc()
        voltage = 3.3 / 256 * digit
        print(digit, voltage)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()