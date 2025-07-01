def get_login(first_name: str, second_name: str) -> str:
  return f'{second_name[:4]}{first_name[0]}'

def test_get_login():
  assert get_login('Иван', 'Иванов') == 'ИванИ'
  assert get_login('Геннадий', 'Петров') == 'ПетрГ'
  assert get_login('Джон', 'Д') == 'ДД'
  assert get_login('Василий', 'Ли') == 'ЛиВ'

test_get_login()
print('Все тесты get_login пройдены')
