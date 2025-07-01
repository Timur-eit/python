from utils.get_login import get_login
from utils.get_user_data_list import get_user_data_list
from utils.get_final_formatted_data import get_final_formatted_data

def app() -> None:
  prompt_user_data = input(f'Введите имя и фамилию через пробел: ')
  first_name, second_name = get_user_data_list(prompt_user_data.title().strip())
  login = get_login(first_name, second_name)

  print(get_final_formatted_data(first_name, second_name, login))

# Project 1_1B
app()
