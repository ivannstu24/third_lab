import math

# Function to calculate temperatures over time
def calculate_temperature(initial_temp, final_temp, rate, duration):
    temperatures = []
    for i in range(duration + 1):
        temperatures.append(final_temp + (initial_temp - final_temp) * math.exp(-rate * i))
    return temperatures

# Function for linear approximation
def linear_approximation(x, y):
    n = len(x)
    xy_sum = sum(xi * yi for xi, yi in zip(x, y))
    x_sum = sum(x)
    y_sum = sum(y)
    x_squared_sum = sum(xi ** 2 for xi in x)
    slope = (n * xy_sum - x_sum * y_sum) / (n * x_squared_sum - x_sum ** 2)
    intercept = (y_sum - slope * x_sum) / n
    return slope, intercept

# Function to calculate correlation coefficient
def correlation_coefficient(x, y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    covariance = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    deviation_x = sum((xi - mean_x) ** 2 for xi in x)
    deviation_y = sum((yi - mean_y) ** 2 for yi in y)
    normalization = math.sqrt(deviation_x * deviation_y)
    return covariance / normalization

def main():
    # User input for parameters
    initial_temp = int(input("Enter initial temperature (T): "))
    final_temp = int(input("Enter final temperature (Ts): "))
    rate = float(input("Enter rate of change (r): "))
    duration = int(input("Enter duration (time): "))

    # Calculate temperatures
    temperatures = calculate_temperature(initial_temp, final_temp, rate, duration)

    # Generate time points
    times = list(range(duration + 1))

    # Perform linear approximation
    slope, intercept = linear_approximation(times, temperatures)
    correlation = correlation_coefficient(times, temperatures)

    # Output results in a tabular format
    print("-------------------------------------------")
    print("| Time (s) | Temperature (C) |")
    print("-------------------------------------------")
    for time, temp in zip(times, temperatures):
        print(f"| {time:^9} | {temp:^15.2f} |")
    print("-------------------------------------------")
    print(f"| Slope (a)        | {slope:^15.2f} |")
    print(f"| Intercept (b)    | {intercept:^15.2f} |")
    print(f"| Correlation (r)  | {correlation:^15.2f} |")
    print("-------------------------------------------")

if __name__ == "__main__":
    main()
