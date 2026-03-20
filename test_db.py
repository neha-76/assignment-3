from pymongo import MongoClient

# paste your connection string here
client = MongoClient("mongodb+srv://neharaj3025_db_user:14JeW9gWCRHVTMWx@cluster0.qqjpn7q.mongodb.net/?appName=Cluster0")

db = client["med_recon"]

print("Connected successfully!")