"""import random
import math


def test_miller(number, coprimes, trials):
    number_minus_one = number - 1
    divisors = []
    for i in range(len(coprimes)):
        if number_minus_one == 0 or coprimes[i] > number_minus_one:
            break
        if number_minus_one % coprimes[i] == 0:
            divisors.append(coprimes[i])
            while number_minus_one % coprimes[i] == 0 and number_minus_one != 0:
                number_minus_one = number_minus_one // coprimes[i]
    random_nums = []
    while len(random_nums) != trials:
        random_num = random.randint(2, number)
        if random_num not in random_nums:
            random_nums.append(random_num)
    for random_num in random_nums:
        result = random_num % number
        for _ in range(2, number):
            result *= random_num
            result = result % number
        if result != 1:
            return " - composite number", 0

    for divisor in divisors:
        flag = True
        for random_num in random_nums:
            result = random_num % number
            for _ in range(2, (number - 1) // divisor + 1):
                result = random_num * result
                result = result % number
            if result != 1:
                flag = False
                break
        if flag:
            return " - composite number", 0
    return " - prime number", 1


def sieve(limit):
    all_numbers = list(range(2, limit + 1))
    primes = []
    while all_numbers:
        current_prime = all_numbers[0]
        primes.append(current_prime)
        all_numbers = [x for x in all_numbers if x % current_prime != 0]
    return primes


def build_miller(bit_length, coprimes, trials):
    while True:
        upper_limit = 0
        z = 1
        f = True
        selected_nums = []
        while f and len(selected_nums) < 1:
            z = 1
            for i in range(len(coprimes)):
                if coprimes[i] > pow(2, bit_length - 1) - 1:
                    break
                max_value = int(math.log(pow(2, bit_length - 1), coprimes[i]))
                random_power = random.randint(1, max_value)
                random_num = random.randint(0, random_power)
                z *= pow(coprimes[i], random_num)
                if z > pow(2, bit_length - 1) - 1:
                    z //= pow(coprimes[i], random_num)
                    if z >= pow(2, bit_length - 2):
                        if z not in selected_nums:
                            selected_nums.append(z)
                        z = 1
                        f = False
        m = random.choice(selected_nums)
        number = 2 * m - 1
        result = test_miller(number, coprimes, trials)
        additional_info = ''
        if result[1] == 1:
            res = test_miller(number, coprimes, 1)
            if res[1] == 0:
                additional_info = '-'
            else:
                additional_info = "+"
        else:
            res = test_miller(number, coprimes, 1)
            if res[1] == 1:
                upper_limit += 1
        if result[1] == 1:
            return additional_info, number, upper_limit


def main():
    bit_length = int(input("Enter the number of bits: "))
    coprimes = sieve(500)
    miller_results = []
    miller_results_primes = []
    while len(miller_results) != 10:
        miller_result = build_miller(bit_length, coprimes, 10)
        prime_num = miller_result[1]
        if prime_num not in miller_results_primes:
            miller_results_primes.append(prime_num)
            miller_results.append(miller_result)
    print("+", end="")
    for _ in range(10):
        print("--------+", end="")
    print("\n|", end="")
    for i in range(10):
        print(f"{i + 1:8}|", end="")
    print("\n+", end="")
    for _ in range(10):
        print("--------+", end="")
    print("\n|", end="")
    for i in range(10):
        print(f"{miller_results[i][1]:8}|", end="")
    print("\n+", end="")
    for _ in range(10):
        print("--------+", end="")
    print("\n|", end="")
    for i in range(10):
        print(f"       {miller_results[i][0]}|", end="")
    print("\n+", end="")
    for _ in range(10):
        print("--------+", end="")
    print("\n|", end="")
    for i in range(10):
        print(f"{miller_results[i][2]:8}|", end="")
    print("\n+", end="")
    for _ in range(10):
        print("--------+", end="")
    print()


if __name__ == "__main__":
    main()
"""