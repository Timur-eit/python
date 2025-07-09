import argparse
import os
from datetime import datetime

# https://docs.python.org/3/library/argparse.html


def copy_csv_and_log(file_paths, output_dir="output", log_file="log.txt"):
    """
    Принимает списка адресов CSV-файлов в файловой системе
    Копирует содержимое файлов в отдельный текстовый файл с префиксом текущей даты и времени.
    Все действия и ошибки записываются в лог-файл.

    :param file_paths: Список имён файлов CSV (можно без пути, если в текущей директории).
    :param output_dir: Папка, куда сохраняются копии (будет создана при необходимости).
    :param log_file: Путь к файлу журнала.
    """
    os.makedirs(output_dir, exist_ok=True)

    current_time_string = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_path = os.path.join(output_dir, f"{current_time_string}_merged_output.txt")

    # with для работы с контекстом + автоматически закрывает файлы
    # операции в with идут друг за другомы
    # open открыть файл
    # режимы:
    # "a" - append (добавляет в конец файла)
    # "w" – write
    with (
        open(log_file, "a", encoding="utf-8") as log,
        open(output_path, "w", encoding="utf-8") as out,
    ):
        for filename in file_paths:
            try:
                # вложенный контекст
                # верхний with открывает и пишет новые файлы,
                # этот контекст работает со списком файлов из списка
                with open(filename, "r", encoding="utf-8") as file_from_list:
                    content = file_from_list.read()
                    out.write(f"--- Содержимое файла {filename}: ---\n")
                    out.write(content)
                    out.write("\n")

                log.write(f"[{datetime.now()}] Скопирован файл: {filename}\n")

            except FileNotFoundError:
                log.write(f"[{datetime.now()}] (!) Error: Файл не найден: {filename}\n")

        log.write(
            f"[{datetime.now()}] Все доступные файлы скопированы в: {output_path}\n"
        )


if __name__ == "__main__":

    # copy_csv_and_log(["data1.csv", "data2.csv", "missing_file.csv"])

    # для работы через CLI:

    # для работы --help
    parser = argparse.ArgumentParser(
        prog="copy_csv_and_log",
        description="Скопировать содержимое CSV-файлов в один текстовый файл.",
        epilog="""
        Какой-то текст в конце help:
        Пример запуска: python csv_merge_log.py data1.csv data2.csv
        """,
    )

    parser.add_argument("files", nargs="+", help="Список CSV-файлов через пробел")
    args = parser.parse_args()

    copy_csv_and_log(args.files)
