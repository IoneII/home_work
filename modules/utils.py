from pathlib import Path
import pyperclip

def log_code(filename="data/log_code.txt"):
    """
    Добавляет содержимое буфера обмена в файл (с новой строки).
    Файл создаётся в текущей папке, если его нет.
    """
    # Получаем текст из буфера обмена
    text = pyperclip.paste().strip()

    # Если буфер пуст — просто пропускаем
    if not text:
        print("⚠ Буфер обмена пуст.")
        return

    # Относительный путь (файл будет рядом со скриптом)
    file_path = Path(__file__).parent.parent / filename

    # Добавляем содержимое с новой строки
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"✅ Текст добавлен в файл: {file_path}")