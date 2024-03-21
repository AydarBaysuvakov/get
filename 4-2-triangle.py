import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]


try:
    t = float(input("Введите период сигнала:")) / 512
    while (True):
        for i in range(255):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(t)
        for i in range(255, 1, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(t)
except ValueError:
    print("Введено неверное значение")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()