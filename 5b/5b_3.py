def get_power_iterative(base: float, exponent: int) -> float:
    """
    Возводит число в степень итеративно.

    :param base: основание
    :param exponent: показатель степени
    :return: результат base ** exponent
    """
    result: float = 1.0
    for _ in range(abs(exponent)):
        result *= base
    return result if exponent >= 0 else 1 / result


def get_power_recursive(base: float, exponent: int) -> float:
    """
    Возводит число в степень рекурсивно.

    :param base: основание
    :param exponent: показатель степени
    :return: результат base ** exponent
    """
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / get_power_recursive(base, -exponent)
    else:
        return base * get_power_recursive(base, exponent - 1)


base = float(input("Введите основание: "))
exponent = int(input("Введите показатель степени: "))

print(f"Итеративно: {get_power_iterative(base, exponent):.2f}")
print(f"Рекурсивно: {get_power_recursive(base, exponent):.2f}")
