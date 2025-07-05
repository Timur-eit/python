words = []

while True:
    word = input("Введите слово (или пустую строку для окончания): ")
    if word == "":
        break
    words.append(word)

result = "".join(w[0] for w in words if w)  # if w — на случай случайных пустых строк

print("Слово-акростих:", result)
