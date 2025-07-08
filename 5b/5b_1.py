from typing import Union

INTERVAL = 5  # в часах


def get_average_temperature(temperature_list: list[Union[float, None]]) -> float:
    """
    Вычисляет среднюю температуру, исключая None (ошибочные записи).

    :param data: список температурных значений, в котором могут быть None
    :return: среднее арифметическое по определённым температурам
    """
    cleaned_data = [
        temperature_item
        for temperature_item in temperature_list
        if temperature_item is not None
    ]

    if not cleaned_data:
        return 0.0

    return sum(cleaned_data) / len(cleaned_data)


temperature_data_list: list[Union[float, None]] = []

for i in range(INTERVAL):
    while True:
        try:
            raw_input = input(f"Введите значение температуры в {i + 1}й час: ")
            if raw_input.strip() == "":
                temperature_data_list.append(None)
                break
            else:
                number_value = float(raw_input)
                temperature_data_list.append(number_value)
                break
        except ValueError:
            print("Ошибка: введите число!")


avg = get_average_temperature(temperature_data_list)
print(f"Средняя температура: {avg:.2f}")
