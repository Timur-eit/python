from typing import Any

rec: dict[str, Any] = {
    "name": {"firstname": "Bob", "lastname": "Smith"},
    "job": ["dev", "mgr"],
    "age": 25,
}

print("Полное имя:", rec["name"]["firstname"], rec["name"]["lastname"])
print("Имя:", rec["name"]["firstname"])
print("Должности:", rec["job"])


rec["job"].append("tester")
print("Список должностей после добавления:", rec["job"])

print("\n")
print("=== Полная информация о персоне ===")
print("Имя:", rec["name"]["firstname"])
print("Фамилия:", rec["name"]["lastname"])
print("Возраст:", rec["age"])
print("Должности:", ", ".join(rec["job"]))
