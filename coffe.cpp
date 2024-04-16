

#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

// Функция для решения дифференциального уравнения методом Эйлера
void cofe(double Tk, double Ts, double r, double dt, int steps, std::vector<double>& x, std::vector<double>& y) {
    x.push_back(0); // Начальное время
    y.push_back(Tk); // Начальная температура кофе

    for (int i = 1; i <= steps; ++i) {
        double dTdt = -r * (y[i - 1] - Ts); // Вычисление производной температуры
        y.push_back(y[i - 1] + dTdt * dt); // Вычисление новой температуры
        x.push_back(x[i - 1] + dt); // Вычисление нового времени
    }
}

// Функция для вычисления коэффициентов аппроксимирующей прямой
void aprox(const std::vector<double>& x, const std::vector<double>& y, double& a, double& b) {
    double sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;
    int n = x.size();

    for (int i = 0; i < n; ++i) {
        sumX += x[i];
        sumY += y[i];
        sumXY += x[i] * y[i];
        sumX2 += x[i] * x[i];
    }

    double numerator = n * sumXY - sumX * sumY;
    double denominator = n * sumX2 - sumX * sumX;

    a = numerator / denominator;
    b = (sumY - a * sumX) / n;
}

// Функция для вычисления коэффициента корреляции
double korrel(const std::vector<double>& x, const std::vector<double>& y) {
    double sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0, sumY2 = 0;
    int n = x.size();

    for (int i = 0; i < n; ++i) {
        sumX += x[i];
        sumY += y[i];
        sumXY += x[i] * y[i];
        sumX2 += x[i] * x[i];
        sumY2 += y[i] * y[i];
    }

    double srX = sumX / n;
    double srY = sumY / n;
    double numerator = 0, denominatorX = 0, denominatorY = 0;

    for (int i = 0; i < n; ++i) {
        numerator += (x[i] - srX) * (y[i] - srY);
        denominatorX += (x[i] - srX) * (x[i] - srX);
        denominatorY += (y[i] - srY) * (y[i] - srY);
    }

    double denominator = sqrt(denominatorX * denominatorY);

    if (denominator == 0) {
        return 0; // Если знаменатель равен нулю, корреляция не определена
    }

    return numerator / denominator;
}


int main() {
    double Tk, Ts, r, dt;
    int steps;
    std::vector<double> x, y;

    // Ввод необходимых параметров
    std::cout << "Введите начальную температуру кофе: ";
    std::cin >> Tk;
    std::cout << "Введите температуру окружающей среды: ";
    std::cin >> Ts;
    std::cout << "Введите коэффициент остывания: ";
    std::cin >> r;
    std::cout << "Введите шаг времени: ";
    std::cin >> dt;
    std::cout << "Введите количество шагов: ";
    std::cin >> steps;

    // Решение дифференциального уравнения
    cofe(Tk, Ts, r, dt, steps, x, y);

    // Аппроксимация прямой
    double a, b;
    aprox(x, y, a, b);

    // Вычисление коэффициента корреляции
    double r_corr = korrel(x, y);

    // Вывод результатов
    std::cout << "Коэффициенты аппроксимирующей прямой: a = " << a << ", b = " << b << std::endl;
    std::cout << "Коэффициент корреляции: " << r_corr << std::endl;

    // Вывод таблицы значений остывания кофе с корреляцией
    std::cout << std::setw(10) << "Время (s)" << std::setw(15) << "Температура (°C)" << std::setw(15) << "Аппроксимация" << std::endl;
    for (size_t i = 0; i < x.size(); ++i) {
        double y_aprox = a * x[i] + b; // Вычисление значения аппроксимации
        std::cout << std::fixed << std::setprecision(2) << std::setw(10) << x[i]
                  << std::setw(15) << y[i] << std::setw(15) << y_aprox << std::endl;
    }

    return 0;
}


