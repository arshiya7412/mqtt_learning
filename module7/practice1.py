
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

token = os.getenv("MONGODB_URI")

client = MongoClient(token, serverSelectionTimeoutMS=5000)

client.admin.command("ping")
print("MongoDB connected successfully")

db = client["iot-data"]
collection = db["sensor_readings"]
