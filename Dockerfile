# Image de base : Python 3.12
FROM python:3.12-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier les dépendances Python
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet dans l'image
COPY . .

# Commande par défaut (optionnelle)
CMD ["python3"]