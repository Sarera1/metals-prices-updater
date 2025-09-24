import json
from firebase_admin import credentials, initialize_app

# Чтение содержимого файла и вывод на экран
file_path = "serviceAccountKey.json"

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Файл успешно прочитан.")
        print("Первые 100 символов файла:")
        print(content[:100])  # Выводим первые 100 символов для проверки

        # Преобразование содержимого в JSON для проверки формата
        json_data = json.loads(content)
        print("JSON формат валиден.")
    
    # Инициализация Firebase
    cred = credentials.Certificate(file_path)
    initialize_app(cred)
    print("Firebase инициализировано успешно.")
    
except json.JSONDecodeError as e:
    print(f"Ошибка декодирования JSON: {e}")
except FileNotFoundError as e:
    print(f"Ошибка: Файл не найден. {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
