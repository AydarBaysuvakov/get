import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Чтение данных из файлов data.txt и settings.txt
with open("data.txt", "r") as f:
    data = [int(x) for x in f.read().split()]
    N = len(data)
    f.close()
with open("settings.txt", "r") as f:
    T, step = map(float, f.read().split())
    f.close()

# Перевод показаний АЦП в Вольты, номеров отсчётов в секунды
time = np.arange(0, N) * T
voltage = np.array(data) * step

# Название графика, с настройками его месторасположения и переносом текста на следующую строку, если текст слишком длинный
fig, ax = plt.subplots(figsize=(16, 10))
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепочке", loc="center")

# Задание максимальных и минимальных значений для шкалы
ax.axis([0, 12.5, 0, 3])
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

# Наличие сетки (главной и дополнительной), настройка ее цвета и стиля
ax.grid(which='major', color = 'gray')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')

# Подписи осей
ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, с")

# Настройки цвета и формы линии, размера и цвета маркеров, частоты отображений маркеров и легенды
ax.plot(time, voltage, color='red', linewidth=1, label = 'V(t)')
ax.scatter(time[0:N:20], voltage[0:N:20], color='red', s=40)
ax.legend()

# Текст с временем зарядки и разрядки
font = {'size': 16}
max_vlt_time = np.argmax(data) * T
ax.text(8, 1.7, f"Время заряда = {max_vlt_time} c", fontdict=font)
ax.text(8, 1.5, f"Время разряда = {time[-1] - max_vlt_time} c", fontdict=font)

# Сохранение графика в файл в формате .svg
fig.savefig('График.png')
fig.savefig('График.svg')

# Пуш и коммит скрипта в репозиторий.
