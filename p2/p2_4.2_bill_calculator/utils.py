from constants import ONE_HUNDRED, ROUND_NUMBER

def get_added_value(net_order_value: float, add_percent: float) -> float:
  """
  Общая утилита для получения суммы добавленной стоимости (налоги / доп сборы)
  """
  return (net_order_value * (add_percent / ONE_HUNDRED))

def get_formatted_number(value: float, digits = ROUND_NUMBER) -> str:
  """
  Утилита для форматирования строки (по умолчанию 2 знака после запятой)
  """
  return f"{value:,.{digits}f}"


# утилиты и бизнес-логика должны быть покрыты тестами – в идеале должны быть авто-тест
# get_added_value
# print('get_added_value: 100, 10 -> 10', get_added_value(100, 10) == 10)
# print('get_added_value: 100, 20 -> 20', get_added_value(100, 20) == 20)
# print('get_added_value: -100, 20 -> -20', get_added_value(-100, 20) == -20)

# get_formatted_number
# print('get_formatted_number: 100 -> "100.00"', get_formatted_number(100) == '100.00')
# print('get_formatted_number: 100 -> "1,000.00"', get_formatted_number(1000) == '1,000.00')
