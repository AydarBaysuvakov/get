import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.OUT)
GPIO.setup(20, GPIO.IN)

GPIO.output(25, GPIO.input(20))