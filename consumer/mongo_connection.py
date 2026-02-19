import os
from pymongo import MongoClient

host = os.getenv("MONGO_HOST", "localhost")
port = int(os.getenv("MONGO_PORT", "27017"))

MONGO_USER = os.getenv("MONGO_USER","user")        
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "password")   
MONGO_AUTHSOURCE = os.getenv("MONGO_AUTHSOURCE", "admin") 
MONGO_DB = os.getenv("MONGO_DB", "alerts")

client = MongoClient(
    host,
    port,
    username=MONGO_USER,
    password=MONGO_PASSWORD,
    authSource=MONGO_AUTHSOURCE)

db = client["week18"]
collection = db["alerts"]