import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

try:
    while (True):
        a = input("Введите число от 0 до 255:")
        if a == 'q':
            break

        try:
            float(a)
        except:
            print("Вы ввели некорректное значение")
            continue

        a = float(a)
        if a != int(a):
            print("Вы ввели не целое значение!")
            continue
        a = int(a)
        if a < 0:
            print("Вы ввели отрицательное значение!")
            continue
        if a > 255:
            print("Вы ввели слишком большое значение!")
            continue
        GPIO.output(dac, decimal2binary(a))
        print("{:.2f}".format(3.3 / 255 * a))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()