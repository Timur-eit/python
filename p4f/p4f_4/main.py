from pathlib import Path
from sys import argv

if len(argv) < 2:
    print("Укажите имя каталога как аргумент командной строки.")
    exit(1)

dir_name = argv[1]

current_dir = Path(".")
new_dir = current_dir / dir_name
new_dir.mkdir(exist_ok=True)

for file in current_dir.glob("*.txt"):
    target_path = new_dir / file.name
    file.replace(target_path)

print(f"Все .txt файлы перемещены в каталог: {new_dir}")
