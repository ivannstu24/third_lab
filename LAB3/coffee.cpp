#include <cmath>
#include <cstddef>
#include <iostream>
#include <iomanip> // For setw
#include <numeric>
#include <utility>
#include <vector>

using namespace std;

// Function prototypes
vector<double> calculateTemperature(int initialTemp, int finalTemp, float rate, int duration);
pair<double, double> linearApproximation(vector<int> x, vector<double> y);
double correlationCoefficient(vector<int> x, vector<double> y);

int main() {
    // User input for parameters
    int initialTemp, finalTemp, duration;
    float rate;

    cout << "Enter initial temperature (T): ";
    cin >> initialTemp;
    cout << "Enter final temperature (Ts): ";
    cin >> finalTemp;
    cout << "Enter rate of change (r): ";
    cin >> rate;
    cout << "Enter duration (time): ";
    cin >> duration;

    // Calculate temperatures
    vector<double> temperatures = calculateTemperature(initialTemp, finalTemp, rate, duration);

    // Generate time points
    vector<int> times = {};
    for (int i = 0; i <= duration; i++)
        times.push_back(i);

    // Perform linear approximation
    auto [slope, intercept] = linearApproximation(times, temperatures);
    double correlation = correlationCoefficient(times, temperatures);

    // Output results in a tabular format
    cout << "-------------------------------------------" << endl;
    cout << "| Time (s) | Temperature (C)" << setw(10) << "|" << endl;
    cout << "-------------------------------------------" << endl;
    for (size_t i = 0; i < temperatures.size(); i++)
        cout << "| " << setw(8) << times[i] << " | " << setw(14) << temperatures[i] << " |" << endl;
    cout << "-------------------------------------------" << endl;
    cout << "| Slope (a)        | " << setw(14) << slope << " |" << endl;
    cout << "| Intercept (b)    | " << setw(14) << intercept << " |" << endl;
    cout << "| Correlation (r)  | " << setw(14) << correlation << " |" << endl;
    cout << "-------------------------------------------" << endl;

    return 0;
}

// Function to calculate temperatures over time
vector<double> calculateTemperature(int initialTemp, int finalTemp, float rate, int duration) {
    vector<double> temperatures = {};
    for (int i = 0; i <= duration; i++)
        temperatures.push_back(finalTemp + (initialTemp - finalTemp) * exp(-rate * i));
    return temperatures;
}

// Function for linear approximation
pair<double, double> linearApproximation(vector<int> x, vector<double> y) {
    size_t n = x.size();
    double xySum = inner_product(x.begin(), x.end(), y.begin(), 0);
    double xSum = accumulate(x.begin(), x.end(), 0);
    double ySum = accumulate(y.begin(), y.end(), 0);
    double xSquaredSum = inner_product(x.begin(), x.end(), x.begin(), 0);
    double slope = (n * xySum - xSum * ySum) / (n * xSquaredSum - pow(xSum, 2));
    double intercept = (ySum - slope * xSum) / n;
    return {slope, intercept};
}

// Function to calculate correlation coefficient
double correlationCoefficient(vector<int> x, vector<double> y) {
    double meanX = accumulate(x.begin(), x.end(), 0.) / x.size();
    double meanY = accumulate(y.begin(), y.end(), 0.) / y.size();
    double covariance = 0.;
    double deviationX = 0., deviationY = 0.;
    for (size_t i = 0; i < x.size(); i++) {
        covariance += (x[i] - meanX) * (y[i] - meanY);
        deviationX += pow(x[i] - meanX, 2);
        deviationY += pow(y[i] - meanY, 2);
    }
    double normalization = pow(deviationX * deviationY, 0.5);
    return covariance / normalization;
}
