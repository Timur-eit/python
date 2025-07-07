def analyze_file(filepath: str) -> None:
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    letter_count = sum(map(str.isalpha, content))
    word_count = len(content.split())
    line_count = content.count("\n") + (1 if content else 0)

    print("Input file contains:")
    print(f"{letter_count} letters")
    print(f"{word_count} words")
    print(f"{line_count} lines")


analyze_file("./file.txt")
