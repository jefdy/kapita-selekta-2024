from pymongo import MongoClient

# Konfigurasi MongoDB
MONGO_URI = 'mongodb://localhost:27017'
DATABASE_NAME = 'db_kapita'
PRODUCT_COLLECTION = 'products'

# Koneksi ke MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
product_collection = db[PRODUCT_COLLECTION]

