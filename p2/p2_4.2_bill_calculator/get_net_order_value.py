from constants import RUB_SYMBOL

def get_net_order_value() -> float:
  prompt_order_value = input(f'Введите сумму заказа ({RUB_SYMBOL}): ')
  
  try:
    net_order_value = float(prompt_order_value)
  except ValueError:
    raise ValueError(f'Некорректный формат значения суммы "{prompt_order_value}" – введите число, например 12.44')
  
  if net_order_value < 0:
    raise ValueError('Сумма заказа не может быть отрицательной')
  
  return net_order_value