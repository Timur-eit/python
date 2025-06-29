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
