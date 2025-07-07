# Список названий дней недели (можно адаптировать под язык)
days = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
]

# список для хранения продаж
sales = []
total: float = 0

# сбор данных от пользователя
for day in days:
    while True:
        # while True нужен для валидации ввода,
        # чтобы программа не "упала" после некорректного ввода (не число)
        try:
            value = float(input(f"Введите сумму продаж за {day}: "))
            sales.append(value)
            total += value
            break
        except ValueError:
            print("Ошибка: введите число!")


print(f"\nОбщий объем продаж за неделю: {total:.2f}")

sorted_sales = sorted(sales)

print("\nПродажи по возрастанию:")
for amount in sorted_sales:
    print(f"{amount:.2f}")
