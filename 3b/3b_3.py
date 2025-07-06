def acrostic() -> None:
    words_list = []

    while True:
        new_word: str = input("Введите слово или пустую строку для завершения: ")
        if new_word == "":
            break

        words_list.append(new_word)

    first_letters: list[str] = [word[0] for word in words_list if word]
    result = "".join(first_letters)

    print("Слово-акростих:", result)


acrostic()
