import time
import RPi.GPIO as GPIO

leds = [2, 3, 4, 17, 27,22, 18, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

nums = [255, 127, 64, 32, 5, 0, 256, 1, 2, 3, 4]

for elem in nums:
    number = [0] * 8
    num = elem % 256
    binary = int(bin(num)[2:])

    length = len(str(binary))
    j=7
    for i in range(length):
        number[j] = binary % 10
        binary//=10
        j-=1

    print(elem, "->", number)
    GPIO.output(dac, number)
    time.sleep(7.0)

GPIO.output(dac, 0)
GPIO.cleanup()
