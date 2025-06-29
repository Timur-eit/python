# константы для переиспользования, чтобы не дублировать код
FAHRENHEIT = 'F'
CELSIUS = 'C'
ROUND_NUMBER = 2
DEG_SYMBOL = '\u00b0' # значок градусов для лучшего отображению пользователю

# конвертация температуры выделена в отдельную функцию для тестирования и отладки
def temperature_converter(value: float, format: str) -> float:
  """
  value (float): значение температуры;
  format (str): формат:
    'F' — из Цельсия в Фаренгейт,
    'C' — из Фаренгейта в Цельсий.
  """
  
  CELSIUS_OFFSET = 32
  FAHRENHEIT_SCALE = 9 / 5

  format = format.upper()
  
  if format == FAHRENHEIT:
    return round(value * FAHRENHEIT_SCALE + CELSIUS_OFFSET, ROUND_NUMBER)
  elif format == CELSIUS:
    return round((value - CELSIUS_OFFSET) / FAHRENHEIT_SCALE, ROUND_NUMBER)
  else:
    raise ValueError(f'Некорректный формат {format} – должен быть или "F" или "C"')
  
# вспомогательная утилита для type guard
def validate_and_get_float(value):
  try:
    result = float(value)
  except ValueError:
    raise ValueError(f'Некорректный формат значения "{value}" – введите число')
  
  return result
  
# запуск самого приложения выделен в функцию, чтобы не было лишних переменных в глобальной области видимости
def app():
  prompt_celsius = input('Введите температуру в градусах Цельсия: ')
  celsius_value = validate_and_get_float(prompt_celsius)
  fahrenheit_result = temperature_converter(celsius_value, FAHRENHEIT)
  print(fahrenheit_result, DEG_SYMBOL + FAHRENHEIT)
  
  prompt_fahrenheit = input('Введите температуру в градусах Фаренгейта: ')
  fahrenheit_value = validate_and_get_float(prompt_fahrenheit)
  celsius_result = temperature_converter(fahrenheit_value, CELSIUS)
  print(celsius_result, DEG_SYMBOL + CELSIUS)

app()

# для best practice лучше выносить функции в отдельные файлы,
# но в учебных целях для первого задания, думаю, можно оставить так, мы пока не формально
# не проходили модули – в след задании попробую сделать


