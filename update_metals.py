import firebase_admin
from firebase_admin import credentials, db


if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://metals-prices-27b05-default-rtdb.firebaseio.com/'
    })


data = {
    "gold": 1925.30,
    "silver": 24.56,
    "platinum": 894.10
}


ref = db.reference("/metals")
ref.set(data)

print("✅ Дані оновлено у Firebase")
