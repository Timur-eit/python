a = int(input("Задайте первое число: "))
b = int(input("Задайте второе число: "))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

nod = a
print("НОД равен", nod)
