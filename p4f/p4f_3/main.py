from pathlib import Path

""" 1. Создание новой директории m_folder """
# домашняя директория пользователя
# home = Path.home()
# my_folder = home / "my_folder"

# в текущей директории
my_folder = Path("./my_folder")
print(f"Рабочая директория: {Path.cwd()}")
print(f"Создаём в: {my_folder.resolve()}")


if not my_folder.exists():
    my_folder.mkdir()

""" 2. Добавление файлов в директорию"""
file1 = my_folder / "file1.txt"

file1.touch()  # первый способ

(my_folder / "file2.txt").touch()  # второй способ

my_folder.joinpath("image.png").touch()  # третий способ

"""
3. Создание нового каталога внутри my_folder
можно без предварительной проверки методом exists() – для этого
указывают параметр exist
_
ok=True, что означает, что если директория уже
существует, то вызов метода не вызовет исключение проверки
"""
(my_folder / "images").mkdir(exist_ok=True)

""" 4. Перемещение файла изображения в созданный каталог """
for f in my_folder.glob("*.png"):
    path_destination = Path(my_folder / "images") / f.name
    f.replace(path_destination)
