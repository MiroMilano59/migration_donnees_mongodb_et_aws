import pandas as pd
from pymongo import MongoClient
from datetime import datetime

# Connexion MongoDB
uri = "mongodb://MiroslavOCR:Miroslav123@host.docker.internal:27017/"
client = MongoClient(uri)

# Base et collection
db = client["healthcare_db"]
collection = db["patients"]

# Lecture du CSV
df = pd.read_csv("data/healthcare_dataset.csv")

# Nettoyage des noms de colonnes
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

# Conversion des dates
df["date_of_admission"] = pd.to_datetime(df["date_of_admission"])
df["discharge_date"] = pd.to_datetime(df["discharge_date"])

# Transformation en documents MongoDB
documents = df.to_dict(orient='records')

# Insertion
collection.insert_many(documents)

# Création d’index pour optimiser les requêtes
collection.create_index("name")
collection.create_index("gender")
collection.create_index("medical_condition")
collection.create_index("doctor")
collection.create_index("date_of_admission")

print(f"{len(documents)} documents insérés et indexes créés dans MongoDB")