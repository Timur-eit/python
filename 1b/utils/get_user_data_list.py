def get_user_data_list(user_data: str) -> list[str]:
  """
  Форматирование данные - если имя сложное (больше 2 слов)
  """
  data_list = user_data.split(' ')

  length = len(data_list)

  if (length == 2):
    return data_list
  
  if length < 2:
    raise ValueError('Имя Фамилия: некорректные данные ввода ')

  first_name = data_list[0]
  second_name = data_list[-1]

  return [first_name, second_name]

def test_get_user_data_list():
    assert get_user_data_list('Анна Иванова') == ['Анна', 'Иванова']
    assert get_user_data_list('Мария Ван дер Вуден') == ['Мария', 'Вуден']
    assert get_user_data_list('Хосе Мария де ла Крус') == ['Хосе', 'Крус']
    
    try:
      get_user_data_list('Ольга')
      assert False, 'Ожидалось ValueError для короткой строки'
    except ValueError:
      pass

test_get_user_data_list()
print('Все get_user_data_list тесты прошли')
