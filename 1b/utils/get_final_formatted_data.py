def get_final_formatted_data(first_name: str, second_name: str, login: str) -> str:
  return f'{second_name.title()} {first_name.title()}: {login}'

def test_get_final_formatted_data():
  assert get_final_formatted_data('Иван', 'Иванов', 'ивани') == 'Иванов Иван: ивани'
  assert get_final_formatted_data('Геннадий', 'Петров', 'петрг') == 'Петров Геннадий: петрг'

test_get_final_formatted_data()
print('Все тесты get_final_formatted_data пройдены')
