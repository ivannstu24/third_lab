#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

// Функция для решения дифференциального уравнения методом Эйлера
void coffeeTemperature(double initialTemperature, double ambientTemperature, double coolingRate, double timeStep, int steps, std::vector<double>& time, std::vector<double>& temperature) {
    time.push_back(0); // Начальное время
    temperature.push_back(initialTemperature); // Начальная температура кофе

    for (int i = 1; i <= steps; ++i) {
        double dTdt = -coolingRate * (temperature[i - 1] - ambientTemperature); // Вычисление производной температуры
        temperature.push_back(temperature[i - 1] + dTdt * timeStep); // Вычисление новой температуры
        time.push_back(time[i - 1] + timeStep); // Вычисление нового времени
    }
}

// Функция для вычисления коэффициентов аппроксимирующей прямой
void linearApproximation(const std::vector<double>& time, const std::vector<double>& temperature, double& slope, double& intercept) {
    double sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;
    int n = time.size();

    for (int i = 0; i < n; ++i) {
        sumX += time[i];
        sumY += temperature[i];
        sumXY += time[i] * temperature[i];
        sumX2 += time[i] * time[i];
    }

    double numerator = n * sumXY - sumX * sumY;
    double denominator = n * sumX2 - sumX * sumX;

    slope = numerator / denominator;
    intercept = (sumY - slope * sumX) / n;
}

// Функция для вычисления коэффициента корреляции
double correlation(const std::vector<double>& time, const std::vector<double>& temperature) {
    double sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0, sumY2 = 0;
    int n = time.size();

    for (int i = 0; i < n; ++i) {
        sumX += time[i];
        sumY += temperature[i];
        sumXY += time[i] * temperature[i];
        sumX2 += time[i] * time[i];
        sumY2 += temperature[i] * temperature[i];
    }

    double meanX = sumX / n;
    double meanY = sumY / n;
    double numerator = 0, denominatorX = 0, denominatorY = 0;

    for (int i = 0; i < n; ++i) {
        numerator += (time[i] - meanX) * (temperature[i] - meanY);
        denominatorX += (time[i] - meanX) * (time[i] - meanX);
        denominatorY += (temperature[i] - meanY) * (temperature[i] - meanY);
    }

    double denominator = sqrt(denominatorX * denominatorY);

    if (denominator == 0) {
        return 0; // Если знаменатель равен нулю, корреляция не определена
    }

    return numerator / denominator;
}

int main() {
    double initialTemperature, ambientTemperature, coolingRate, timeStep;
    int steps;
    std::vector<double> time, temperature;

    // Ввод необходимых параметров
    std::cout << "Введите начальную температуру кофе: ";
    std::cin >> initialTemperature;
    std::cout << "Введите температуру окружающей среды: ";
    std::cin >> ambientTemperature;
    std::cout << "Введите коэффициент остывания: ";
    std::cin >> coolingRate;
    std::cout << "Введите шаг времени: ";
    std::cin >> timeStep;
    std::cout << "Введите количество шагов: ";
    std::cin >> steps;

    // Решение дифференциального уравнения
    coffeeTemperature(initialTemperature, ambientTemperature, coolingRate, timeStep, steps, time, temperature);

    // Аппроксимация прямой
    double slope, intercept;
    linearApproximation(time, temperature, slope, intercept);

    // Вычисление коэффициента корреляции
    double correlationCoefficient = correlation(time, temperature);

    // Вывод результатов
    std::cout << "Коэффициенты аппроксимирующей прямой: a = " << slope << ", b = " << intercept << std::endl;
    std::cout << "Коэффициент корреляции: " << correlationCoefficient << std::endl;

    // Вывод таблицы значений остывания кофе с корреляцией
    std::cout << std::setw(10) << "Время (s)" << std::setw(15) << "Температура (°C)" << std::setw(15) << "Аппроксимация" << std::endl;
    for (size_t i = 0; i < time.size(); ++i) {
        double approximation = slope * time[i] + intercept; // Вычисление значения аппроксимации
        std::cout << std::fixed << std::setprecision(2) << std::setw(10) << time[i]
                  << std::setw(15) << temperature[i] << std::setw(15) << approximation << std::endl;
    }

    return 0;
}
