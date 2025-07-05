list_of_numbers = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]

list_of_numbers.sort(reverse=True)

print("отсортированный в DESC list_of_numbers", list_of_numbers)

list_of_numbers_sorted_asc = sorted(list_of_numbers)

print("list_of_numbers", list_of_numbers)
print("list_of_numbers_sorted_asc", list_of_numbers_sorted_asc)


# сортировка массива кортежей по числовому значению по индексу 2
student_tuples = [
    ("john", "A", 15),
    ("jane", "B", 12),
    ("dave", "B", 10),
]
print(
    "сортировка массива кортежей",
    sorted(student_tuples, key=lambda student: student[2]),
)


# сортировка массива объектов по полю age
class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return repr({"name": self.name, "age": self.age})


users: list[User] = [
    User("Ivan", 31),
    User("Pavel", 27),
    User("Alexander", 35),
]

print("Исходный список пользователей\n", users)
print("Отсортированный ASC\n", sorted(users, key=lambda user: user.age))
print("Отсортированный DESC\n", sorted(users, key=lambda user: user.age, reverse=True))
