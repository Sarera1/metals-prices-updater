import firebase_admin
from firebase_admin import credentials, db

# --- Ініціалізація Firebase ---
if not firebase_admin._apps:
    # Указываем путь к JSON файлу с ключом
    cred = credentials.Certificate("serviceAccountKey.json")
    
    # Инициализация приложения Firebase с указанием URL базы данных
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://metals-prices-27b05-default-rtdb.europe-west1.firebasedatabase.app/'
    })

# --- Дані для оновлення ---
data = {
    "gold": 1925.30,
    "silver": 24.56,
    "platinum": 894.10
}

# --- Запис у Firebase ---
# Ссылка на базу данных, куда будут записываться данные
ref = db.reference("/metals")
ref.set(data)  # Записываем данные в Firebase

print("✅ Дані оновлено у Firebase")
