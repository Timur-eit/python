from random import randint

num = input("Введите число для подсчета суммы цифр: ")
sumIt = 0
for it in num:
    sumIt += int(it)
print(f"Сумма цифр числа {num} равна {sumIt}")

# Контрольное задание

total = 100  # начальный запас ресурса

for i in range(5):  # цикл на 5 этапов
    n = randint(1, 50)  # имитация расхода
    print(f"Этап {i+1}: расход = {n}, остаток до вычета = {total}")
    total -= n

    if total < 0:
        print(f"Ресурс закончился на этапе {i+1}")
        total = 0
        break

else:
    print("Процесс выполнен полностью")

print("Осталось", total)
