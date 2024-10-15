from typing import List
import random

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

# 4. Функция pipeline, которая выполняет все шаги
def pipeline() -> int:
    primes_list = primes(1000)
    random.seed(100)
    random.shuffle(primes_list)
    return checksum(primes_list)

# 5. Основной блок выполнения
if __name__ == "__main__":
    result = pipeline()
    print(result)