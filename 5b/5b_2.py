INPUT_ITERATION = 8


def get_separate_numbers(*args: float) -> tuple[list[float], list[float]]:
    """
    Разделяет переданные числа на отрицательные и неотрицательные.

    :param args: неограниченное количество числовых аргументов
    :return: кортеж из двух списков: (отрицательные по убыванию, неотрицательные по возрастанию)
    """
    negatives: list[float] = sorted([round(x, 2) for x in args if x < 0], reverse=True)
    non_negatives: list[float] = sorted([round(x, 2) for x in args if x >= 0])
    return (negatives, non_negatives)


numbers: list[float] = []

for i in range(INPUT_ITERATION):
    while True:
        try:
            user_input = float(input(f"Введите {i + 1} число: "))
            numbers.append(user_input)
            break

        except ValueError:
            print("Ошибка: введите число!")


negatives, non_negatives = get_separate_numbers(*numbers)

print("Отрицательные (по убыванию):", negatives)
print("Неотрицательные (по возрастанию):", non_negatives)
