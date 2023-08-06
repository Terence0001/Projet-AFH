# base image
FROM python:3.9.12

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer Node.js
RUN apt-get update && apt-get install -y nodejs npm

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Copier les fichiers de l'application dans le conteneur
COPY . .

# Installer les dépendances de l'application Django
RUN pip install --no-cache-dir -r requirements.txt

# Installer les dépendances de l'application VueJS3
WORKDIR /app/AFH-frontend
RUN npm install

# Construire l'application VueJS3
RUN npm run build

# Retourner au répertoire de travail initial
WORKDIR /app

# Exposer le port 8000 pour accéder à l'application
EXPOSE 8000

# Définir la commande par défaut pour exécuter l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
