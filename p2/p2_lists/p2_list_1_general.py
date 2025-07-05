list_of_numbers = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]

# print(dir(list))
print("исходный список\n", list_of_numbers)

list_of_numbers[0] = 100
print("заменили первый элемент\n", list_of_numbers)

current_third_index_item = list_of_numbers[3]
updated_third_index_item_value = 555
list_of_numbers[3] = updated_third_index_item_value
print(
    f"заменили четвертый элемент {current_third_index_item} на {updated_third_index_item_value}\n",
    list_of_numbers,
)

new_item = 777
list_of_numbers.append(new_item)
print(f"добавили в массив элемент {new_item}\n", list_of_numbers)

current_second_item = list_of_numbers[2]
updated_second_item_value = 5555
list_of_numbers.insert(2, updated_second_item_value)
print(
    f"вставили {updated_second_item_value} на позицию с индексом 2 вместо {current_second_item}\n",
    list_of_numbers,
)

fourth_item = list_of_numbers[4]
del list_of_numbers[4]
print(f"удалили элемент с индексом 4: {fourth_item}\n", list_of_numbers)

last_element = list_of_numbers.pop()
print(
    f"pop() удаляет последний элемент и возвращает его: {last_element}\n",
    list_of_numbers,
)
