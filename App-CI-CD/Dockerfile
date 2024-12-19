# Utiliser une image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY app/ /app
COPY requirements.txt /app

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port 5000
EXPOSE 5000

# Lancer l'application
CMD ["python", "app.py"]
