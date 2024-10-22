from typing import List
import random
import argparse

# 1. Функция проверки простоты числа
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# 2. Функция генерации списка простых чисел
def primes(count: int) -> List[int]:
    primes_list = []
    num = 2
    while len(primes_list) < count:
        if is_prime(num):
            primes_list.append(num)
        num += 1
    return primes_list

# 3. Функция расчёта контрольной суммы
def checksum(x: List[int]) -> int:
    MODULO = 10_000_007
    result = 0
    for number in x:
        result = (result + number) * 113 % MODULO
    return result

# 4. Основная функция, которая принимает параметры из командной строки
def main():
    # Парсим аргументы командной строки
    parser = argparse.ArgumentParser(description="Генерирование листа простых чисел и их микс.")
    parser.add_argument('count', type=int, help="Количество простых чисел")
    parser.add_argument('seed', type=int, help="Любое число для генерации")
    args = parser.parse_args()

    # Генерация простых чисел
    primes_list = primes(args.count)

    # Перемешивание списка
    random.seed(args.seed)
    random.shuffle(primes_list)

    # Печать каждого простого числа на новой строке
    for prime in primes_list:
        print(prime)

if __name__ == "__main__":
    main()
