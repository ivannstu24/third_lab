import random
import math


def resheto(n):
    all_nums = list(range(2, n + 1))
    primes = []
    while all_nums:
        current_prime = all_nums[0]
        primes.append(current_prime)
        all_nums = [x for x in all_nums if x % current_prime != 0]
    return primes


def rn(a, b):
    rand_num = round(random.uniform(a, b), 1)
    return rand_num


def build_new_from_old(q, bit):
    while True:
        zak = rn(0, 1)
        n_val = pow(2, bit - 1) / q + (pow(2, bit - 1) * zak) / q
        if int(n_val) % 2 == 1:
            n_val += 1
        u_val = 0
        while True:
            flg1 = False
            flg2 = False
            p_val = int((n_val + u_val) * q) + 1
            if p_val > pow(2, bit):
                break
            res1 = 2 % int(p_val)
            for i in range(2, int(p_val)):
                res1 *= 2
                res1 = res1 % int(p_val)
            if res1 == 1:
                flg1 = True

            res2 = 2 % int(p_val)
            for i in range(2, int(n_val + u_val + 1)):
                res2 *= 2
                res2 = res2 % int(p_val)
            if res2 != 1:
                flg2 = True
            if flg1 and flg2:
                return int(p_val)
            u_val += 2


def main():
    c_lst = resheto(500)
    bit_num = int(input("Введите количество бит: "))

    print("+", end="")
    for _ in range(10):
        print("--------+", end="")
    print()

    print("|", end="")
    for i in range(10):
        print(f"{i + 1:8}|", end="")
    print()

    print("+", end="")
    for _ in range(10):
        print("--------+", end="")
    print()

    print("|", end="")
    rand_val = random.randint(0, (len(c_lst) - 10) // 10) * 10
    for i in range(10):
        print(f"{build_new_from_old(c_lst[rand_val + i], bit_num):8}|", end="")
    print()

    print("+", end="")
    for _ in range(10):
        print("--------+", end="")
    print()


if __name__ == "__main__":
    main()
