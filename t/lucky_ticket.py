def is_lucky_ticket_str(ticket_number: int) -> bool:
    """
    Проверяет, является ли билетик счастливым –
    сравнить суммы первых трех и вторых трех цифр, если они равны то билет счастливый
    Ожидает 6 цифр.
    """
    NUM_LEN = 6

    converted_to_str_data = str(ticket_number)

    if len(converted_to_str_data) != NUM_LEN or not converted_to_str_data.isdigit():
        raise ValueError("Билет должен содержать ровно 6 цифр.")

    first_three_sum = 0
    second_three_sum = 0

    for i in range(NUM_LEN):
        if i < NUM_LEN // 2:
            first_three_sum += int(converted_to_str_data[i])
        else:
            second_three_sum += int(converted_to_str_data[i])

    return first_three_sum == second_three_sum


def test_is_lucky_ticket_str():
    assert is_lucky_ticket_str(385916) == True
    assert is_lucky_ticket_str(123321) == True
    assert is_lucky_ticket_str(111111) == True
    assert is_lucky_ticket_str(101011) == True

    assert is_lucky_ticket_str(123456) == False
    assert is_lucky_ticket_str(999000) == False
    assert is_lucky_ticket_str(100200) == False
    assert is_lucky_ticket_str(555554) == False


test_is_lucky_ticket_str()
print("Все is_lucky_ticket_str тесты прошли")
