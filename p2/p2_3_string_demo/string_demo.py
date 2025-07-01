string1 = "Это строка."
string2 = " Это тоже строка."

concatenated_result = string1 + string2

# длина строки
print('len(concatenated_result):', len(concatenated_result))

# преобразует первый символ каждого слова в строке к верхнему регистру
print('string2.title():', string2.title())

# символы строки преобразуются к нижнему регистру;
print('string2.lower():', string2.lower())

# символы строки преобразуются к верхнему регистру;
print('string2.upper()', string2.upper())

# удаляются пробелы в конце строки;
print('string2.rstrip()', string2.rstrip())

# удаляются пробелы в начале строки
print('string2.lstrip()', string2.lstrip())

# strip() - удаляются пробелы с обоих концов;
print('string2.strip()', string2.strip())

# удаляются указанные символы в параметре функции.
print('(string2 + "......").strip(".")', (string2 + '......').strip('.'))

# param1 = "string" + 15 ошибка несовместимости типов
param1 = "string" + str(15)
print('param1', param1)

# тоже ошибка
# param2 = 15 +  "25"

param2 = 15 + int('25')
print('param2', param2)

# ++++ работа с форматирование +++

a = 1 / 3
print("{:7.3f}".format(a))

a = 2 / 3
b = 2 / 9
print('{:7.3f} {:7.3f}'.format(a, b))
print('{:10.3e} {:10.3e}'.format(a, b))

print('{:10.3e} {:10.3e}'.format(a, b))

# вариант с f-строкой
print(f'{1000:,.{2}f}') # -> 1,000.00



