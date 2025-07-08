from typing import TypedDict


def get_numbers(iterations: int = 3) -> dict[str, float]:
    if iterations > 25:
        # можно ввести от 'a' до 'z' - 25 итераций
        raise ValueError("Максимальное количество итераций ввода - 25")

    # chr(97) → 'a'
    # chr(97 + 25) → 'z'
    symbol_list = [chr(97 + i) for i in range(iterations)]

    # symbol_list = []
    # for i in range(iterations):
    #     symbol = chr(97 + i)
    #     symbol_list.append(symbol)

    numbers: dict[str, float] = {}

    for key in symbol_list:
        new_number = float(input(f"Введите число {key}: "))
        numbers[key] = new_number

    return numbers


class Numbers(TypedDict):
    min: float
    max: float
    total: float
    rounded: float


def calculate_number(numbers: dict[str, float], round_digits: int = 2) -> Numbers:
    min_number = min(numbers.values())
    max_number = max(numbers.values())
    total = sum(numbers.values())
    rounded_total = round(total, round_digits)

    return {
        "min": min_number,
        "max": max_number,
        "total": total,
        "rounded": rounded_total,
    }


def print_output(numbers: Numbers, round_digits: int = 2) -> None:

    output = f"""
    Минимальное значение: {numbers['min']}
    Максимальное значение: {numbers['max']}
    Сумма: {numbers['total']}
    Сумма после округления до 2 знаков: {numbers['rounded']:,.{round_digits}f}
    """

    print(output)


print_output(calculate_number(get_numbers()))
