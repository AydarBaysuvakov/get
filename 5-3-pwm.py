import RPi.GPIO as GPIO

outp = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(outp, GPIO.OUT)

p = GPIO.PWM(outp, 50)
p.start(0)

try:
    while (True):
        a = float(input("Введите коэфицент заполнения:"))
        p.ChangeDutyCycle(a)
        print("{:.2f}".format(3.3 / 100 * a))
finally:
    p.stop()
    GPIO.cleanup()