# 1. Image de base officielle Python
FROM python:3.10-slim

# 2. Dossier de travail dans le conteneur
WORKDIR /app

# 3. Copier le script de migration et le fichier .env
COPY mongo/migrate_to_mongo.py .
COPY ../.env .env

# 4. Installer les dépendances Python
RUN pip install pandas pymongo python-dotenv

# 5. Point d’entrée du conteneur
CMD ["python", "migrate_to_mongo.py"]