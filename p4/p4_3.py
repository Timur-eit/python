from random import randint

total = 100
i = 0
while i < 5:
    n = randint(1, 50)
    total = total - n
    if total < 0:
        total = 0
        break
    i = i + 1
else:
    print("Процесс выполнен полностью")

print("Осталось", total)
