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
    sig = 0
    for i in range(8):
        GPIO.output(dac, decimal2binary(sig + 2 ** (7 - i)))
        if not GPIO.input(comp):
            sig += 2 ** (7 - i)
        time.sleep(0.005)
    return sig
        

try:
    while True:
        digit = adc()
        voltage = 3.3 / 256 * digit
        print(digit, voltage)
        time.sleep(1)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()