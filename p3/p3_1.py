def get_max() -> None:
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    third = int(input("Введите третье число: "))

    if first >= second and first >= third:
        max_number = first
    elif second >= first and second >= third:
        max_number = second
    else:
        max_number = third

    # или просто
    # max_number = max(first, second, third)

    print("Наибольшее число:", max_number)


get_max()
