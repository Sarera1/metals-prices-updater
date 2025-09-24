import firebase_admin
from firebase_admin import credentials, db
import os
import json

# Чтение ключа Firebase из переменной окружения
firebase_key = os.environ.get('FIREBASE_KEY')

if not firebase_key:
    raise ValueError("Не найден Firebase ключ в переменных окружения!")

# Преобразуем строку JSON в словарь
cred_dict = json.loads(firebase_key)

# Инициализация Firebase
cred = credentials.Certificate(cred_dict)

# Если Firebase не инициализировано, инициализируем
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://metals-prices-27b05-default-rtdb.firebaseio.com/'
    })

# Данные для обновления
data = {
    "gold": 1925.30,
    "silver": 24.56,
    "platinum": 894.10
}

# Запись в Firebase
ref = db.reference("/metals")
ref.set(data)

print("✅ Дані оновлено у Firebase")
