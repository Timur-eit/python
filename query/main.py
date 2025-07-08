# from urllib.parse import quote_plus
# https://docs.python.org/3/library/urllib.parse.html
# Example: quote_plus('/El Niño/') yields '%2FEl+Ni%C3%B1o%2F'.


def make_query(**kwargs) -> str:
    """
    Формирует строку запроса из произвольного количества именованных аргументов.
    Ключи сортируются в алфавитном порядке.

    :param kwargs: именованные параметры
    :return: строка в формате key1=value1&key2=value2&...
    """
    sorted_items = sorted(kwargs.items())  # kwargs.items() похож на Object.entries(obj)

    query_parts = [
        # в проде использовать с quote_plus
        # f"{quote_plus(key)}={quote_plus(str(value))}" for (key, value) in sorted_items
        f"{key}={value}"
        for (key, value) in sorted_items
    ]
    return "&".join(query_parts)


sample_a = make_query(category="books", genre="thriller", author="Stephen_King")
sample_b = make_query(name="Егор", last_name="Тимохин", age=25, occupation="дизайнер")

print(sample_a)
print(sample_b)

assert sample_a == "author=Stephen_King&category=books&genre=thriller"
assert (
    make_query(name="Егор", last_name="Тимохин", age=25, occupation="дизайнер")
    == "age=25&last_name=Тимохин&name=Егор&occupation=дизайнер"
)
print("Все тесты make_query пройдены")
