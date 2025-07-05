import random

# списковое включение
numbers = [random.randint(1, 100) for _ in range(10)]

threshold = 50

labels = ["High" if num > threshold else "Low" for num in numbers]


print("Исходный список:", numbers)
print("Список High/Low:", labels)
