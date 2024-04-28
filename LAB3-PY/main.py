"""

import math

def main():
    dx = 0.5
    r1 = 1
    r2 = 2
    print("Значения функции")
    print("________________________________________")
    print('| {:^10} | {:^10} |'.format('X', 'Y'))
    print("________________________________________")
    for x in [x * dx for x in range(-6, 15)]:
        if -3 <= x <= -2:
            y = -x - 2
        elif -2 < x <= 0:
            y = math.sqrt(r1 ** 2 - (x + 1) ** 2)
        elif 0 < x <= 4:
            y = -1 * math.sqrt(r2 ** 2 - (x - 2) ** 2)
        elif 4 < x <= 6:
            y = (-x / 4 + 1) * 2
        elif 6 < x <= 7:
            y = -1
        print('| {:10.3f} | {:10.3f} |'.format(x, y))
    print("________________________________________")

if __name__ == "__main__":
    main()
"""


