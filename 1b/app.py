from utils.get_login import get_login
from utils.get_user_data_list import get_user_data_list
from utils.get_final_formatted_data import get_final_formatted_data

def app() -> None:
  prompt_user_data = input(f'Введите имя и фамилию через пробел: ')
  name, surname = get_user_data_list(prompt_user_data.title())
  login = get_login(name, surname)

  print(get_final_formatted_data(name, surname, login))

# Project 1_1B
app()

    
  

  




  