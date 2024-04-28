import random
import math

def sieve(n):
    all_numbers = list(range(2, n + 1))
    primes = []
    while all_numbers:
        current_prime = all_numbers[0]
        primes.append(current_prime)
        all_numbers = [x for x in all_numbers if x % current_prime != 0]
    return primes

def random_number(a, n):
    return random.randint(a, n)

def test_prime(n, divisors, t):
    random_numbers = []
    while len(random_numbers) != t:
        random_num = random_number(2, n - 1)
        if random_num not in random_numbers:
            random_numbers.append(random_num)
    for random_num in random_numbers:
        result = random_num % n
        for _ in range(2, n):
            result = result * random_num
            result = result % n
        if result != 1:
            return " - composite number", 0
    n32 = n - 1
    for j in random_numbers:
        for d in divisors:
            quotient = n32 // d
            result2 = j % n
            for _ in range(2, quotient + 1):
                result2 = result2 * j
                result2 = result2 % n
            if result2 == 1:
                break
        else:
            return " - prime number", 1
    return " - probably composite number", 0

def build_prime(bit, c, t):
    composite_count = 0
    while True:
        z = 1
        f = True
        geted = []
        divisors = []
        while f and len(geted) < 1:
            z = 1
            divisors_temp = []
            for i in range(len(c)):
                if c[i] > pow(2, bit // 2 + 1) - 1:
                    break
                max_val = int(math.log(pow(2, bit // 2 + 1), c[i]))
                rpow = random_number(1, max_val)
                rnum = random_number(0, rpow + 1)
                z *= pow(c[i], rnum)
                if z > pow(2, bit // 2):
                    z //= pow(c[i], rnum)
                    if z >= pow(2, bit // 2):
                        if z not in geted:
                            geted.append(z)
                        z = 1
                        f = False
                        divisors = divisors_temp[:]
                else:
                    if rnum:
                        divisors_temp.append(c[i])
        n = random_number(pow(2, bit // 2 - 1), pow(2, bit // 2) - 1) * geted[0] + 1
        result = test_prime(n, divisors, t)
        oleg = ''
        if result[1] == 1:
            res = test_prime(n, c, 1)
            if res[1] == 1:
                oleg = '+'
            else:
                oleg = '-'
        else:
            res = test_prime(n, c, 1)
            if res[1] == 1:
                composite_count += 1
        if result[1] == 1:
            return oleg, n, composite_count

def main():
    bit = int(input("Enter number of bits: "))
    c = sieve(500)
    result_list = []
    result_list_p = []
    test_prime(13, [2], 10)
    while len(result_list_p) != 10:
        result = build_prime(bit, c, 10)
        p = result[1]
        if p not in result_list_p:
            result_list_p.append(p)
            result_list.append(result)
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
        print(f"{result_list[i][1]:8}|", end="")
    print("\n+", end="")
    for _ in range(10):
        print("--------+", end="")
    print("\n|", end="")
    for i in range(10):
        print(f"       {result_list[i][0]}|", end="")
    print("\n+", end="")
    for _ in range(10):
        print("--------+", end="")
    print("\n|", end="")
    for i in range(10):
        print(f"{result_list[i][2]:8}|", end="")
    print("\n+", end="")
    for _ in range(10):
        print("--------+", end="")
    print()

if __name__ == "__main__":
    main()
