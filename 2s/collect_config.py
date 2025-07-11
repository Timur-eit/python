from netmiko import ConnectHandler
from datetime import datetime

devices = [
    # см конфиг в ./notes.md
    {
        "device_type": "linux",
        "host": "localhost",
        "port": 2222,
        "username": "admin",
        "password": "admin",
    }
]


def collect_config(device):
    """
    Подключается c помощью netmiko по SSH к устройству / контейнеру
    Выполняет `uname -a`
    Сохраняет вывод в лог файл с меткой времени
    """
    try:
        # **device распаковывает словарь и передаёт его ключи как именованные аргументы
        connection = ConnectHandler(**device)
        prompt = connection.find_prompt()
        # uname -a: Отображает сведения о системе (тестовая команда)
        # Параметр expect_string сообщает netmiko, какое приглашение (prompt) ждать после выполнения команды, чтобы понять, что вывод завершился.
        output = connection.send_command("uname -a", expect_string=r"\$ ")

        print(f"\n{prompt} Конфигурация:\n")
        print(output)

        log_file_name = (
            f"{device['host']}_config_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
        with open(log_file_name, "w", encoding="utf-8") as log_file:
            log_file.write(str(output))

        connection.disconnect()

    except Exception as exception:
        print(f"ERROR! Не удалось подключиться к {device['host']}: {exception}")


if __name__ == "__main__":
    for device in devices:
        collect_config(device)
