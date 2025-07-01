def get_login(first_name: str, second_name: str) -> str:
  return f'{second_name[:4]}{first_name[0]}'.lower()

def test_get_login():
  assert get_login('Иван', 'Иванов') == 'ивани'
  assert get_login('Геннадий', 'Петров') == 'петрг'
  assert get_login('Джон', 'Д') == 'дд'
  assert get_login('Василий', 'Ли') == 'лив'

test_get_login()
print('Все тесты get_login пройдены')
