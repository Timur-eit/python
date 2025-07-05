from typing import Any

dict_sample: dict[str, Any] = {"food": "Apple", "quantity": 4, "color": "Red"}

print("food", dict_sample["food"])

dict_sample["food"] = "Pineapple"
print("food", dict_sample["food"])

print("quantity", dict_sample["quantity"])

dict_sample["quantity"] += 10
print("quantity", dict_sample["quantity"])

dp: dict[str, Any] = {}

dp["name"] = input("Введите имя: ")
dp["age"] = int(input("Введите возраст: "))

print("Ваш словарь:", dp)
