n = int(input("Задайте число: "))
k = 0
digit_sum = 0

while n > 0:
    digit = n % 10
    digit_sum += digit
    n = n // 10  #  отбрасываем последнюю цифру
    k += 1

print("Количество цифр в числе:", k)
print("Сумма цифр числа:", digit_sum)
