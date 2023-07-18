# Voici ci-dessous les instructions pour bien démarrer le projet AFH

#### **[Retour à l'introduction du projet ?](./README.md)**

Ces dernières vont vous permettre de créer un environnement virtuel, y installer les bonnes dépendances, le faire fonctionner et aussi utiliser un conteneur Docker

**1. Création de l'environnement virtuel**

Ce dernier ira contenir toutes nos dépendances (Paquets)\
Utiliser la commande suivante dans votre terminal (Powershell) :

```sh
python -m venv ./venv
```

---

**2. Activation de l'environnement virtuel**

Avec Powershell

```sh
.\venv\Scripts\activate
```

ou avec CMD

```sh
.\venv\Scripts\activate.bat
```

Pour le désactiver utiliser la commande suivante si-besoin:

```sh
deactivate
```

---

**3. Instalation des dépendances (Ou paquets) dans l'environnement virtuel**

```sh
pip install -r requirements.txt
```

---

**4. Navigation dans le dossier backend**

```sh
cd .\backend\
```

---

**5. Démarage du serveur backend**

```sh
py manage.py runserver
```

---

**6. Migrer les données de la base de données**

```sh
py manage.py migrate
```
