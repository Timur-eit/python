import math


def get_sqrt(number: float) -> int:
    return math.ceil(math.sqrt(number))


number = float(input("Введите число: "))

print("get_sqrt(a) = ", get_sqrt(number))
