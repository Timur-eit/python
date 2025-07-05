# print(dir(tuple))
# help(tuple.index)
# help(tuple.count)

seq = (2, 8, 23, 97, 92, 44, 17, 39, 11, 12)

print("Количество повторений значения 8 в seq", seq.count(8))
print("Индекс значения 44 в seq", seq.index(44))

list_seq = list(seq)
print(type(list_seq), list_seq)

print("sorted DESC", sorted(list_seq, reverse=True))
