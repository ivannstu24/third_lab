import numpy as np

# Функция для решения дифференциального уравнения методом Эйлера
def coffee_temperature(initial_temperature, ambient_temperature, cooling_rate, time_step, steps):
    time = [0]  # Начальное время
    temperature = [initial_temperature]  # Начальная температура кофе

    for i in range(1, steps + 1):
        dTdt = -cooling_rate * (temperature[i - 1] - ambient_temperature)  # Вычисление производной температуры
        temperature.append(temperature[i - 1] + dTdt * time_step)  # Вычисление новой температуры
        time.append(time[i - 1] + time_step)  # Вычисление нового времени

    return time, temperature

# Функция для вычисления коэффициентов аппроксимирующей прямой
def linear_approximation(time, temperature):
    X = np.array(time)
    Y = np.array(temperature)
    n = len(time)

    sumX = np.sum(X)
    sumY = np.sum(Y)
    sumXY = np.sum(X * Y)
    sumX2 = np.sum(X ** 2)

    numerator = n * sumXY - sumX * sumY
    denominator = n * sumX2 - sumX ** 2

    slope = numerator / denominator
    intercept = (sumY - slope * sumX) / n

    return slope, intercept

# Функция для вычисления коэффициента корреляции
def correlation(time, temperature):
    X = np.array(time)
    Y = np.array(temperature)
    n = len(time)

    meanX = np.mean(X)
    meanY = np.mean(Y)

    numerator = np.sum((X - meanX) * (Y - meanY))
    denominatorX = np.sum((X - meanX) ** 2)
    denominatorY = np.sum((Y - meanY) ** 2)

    denominator = np.sqrt(denominatorX * denominatorY)

    if denominator == 0:
        return 0  # Если знаменатель равен нулю, корреляция не определена

    return numerator / denominator

# Ввод необходимых параметров
initial_temperature = float(input("Введите начальную температуру кофе: "))
ambient_temperature = float(input("Введите температуру окружающей среды: "))
cooling_rate = float(input("Введите коэффициент остывания: "))
time_step = float(input("Введите шаг времени: "))
steps = int(input("Введите количество шагов: "))

# Решение дифференциального уравнения
time, temperature = coffee_temperature(initial_temperature, ambient_temperature, cooling_rate, time_step, steps)

# Аппроксимация прямой
slope, intercept = linear_approximation(time, temperature)

# Вычисление коэффициента корреляции
correlation_coefficient = correlation(time, temperature)

# Вывод результатов
print("Коэффициенты аппроксимирующей прямой: a =", slope, ", b =", intercept)
print("Коэффициент корреляции:", correlation_coefficient)

# Вывод таблицы значений остывания кофе с корреляцией
print("{:<10} {:>15} {:>15}".format("Время (s)", "Температура (°C)", "Аппроксимация"))

for i in range(len(time)):
    approximation = slope * time[i] + intercept  # Вычисление значения аппроксимации
    print("{:<10.2f} {:>15.2f} {:>15.2f}".format(time[i], temperature[i], approximation))
