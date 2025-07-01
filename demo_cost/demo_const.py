'''
Задача. Требуется вычислить значение стоимости в зависимости от условия
Предлагается решение без применения if'''

'''Используется преобразование типа при арифметической операции
и операции сравнения'''

# rate = 0.18
# cost = 100
# cost = cost + cost * rate * (rate > 0.13)
# print(cost) # 118.0


''' Задание
Для диапазона условие:
    если параметр больше 5 и меньше или равен 30, то (a - 5) * 1.2
    если параметр больше 30, то (a - 30) * 1.5'''

# a = 40 # тестовое значение
# y = 0 # укажите требуемое выражение
# print(y) # 15.0

def get_demo_const(number_param: float) -> float:
    """
    Возвращает значение по правилам:
      - если number_param > 5 и number_param <= 30, то (number_param - 5) * 1.2
      - если number_param > 30, то (number_param - 30) * 1.5
      - иначе: 0
    Решение без if, только арифметика и сравнения.
    """
    return (
         ((number_param - 5) * 1.2) * (number_param > 5 and number_param <= 30)
         +
         ((number_param - 30) * 1.5) * (number_param > 30)
    )

def test_get_demo_const():
    assert get_demo_const(40) == 15.0
    assert get_demo_const(20) == 18.0
    assert get_demo_const(5) == 0.0
    assert get_demo_const(31) == 1.5
    assert get_demo_const(-10) == 0.0
    
test_get_demo_const()
print('Все тесты get_demo_const прошли')
