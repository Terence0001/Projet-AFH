# Projet AFH

 <img src="./Pictures/Logo.png" alt="Logo" width="400">

## Projet d’Analyse de Fertilité des Hommes.

## Sommaire

1. [Objectifs du projet](#voici-les-objectifs-primordiaux-de-ce-projet)
2. [Livrables attendus](#Livrables-attendus)
3. [Instructions pour bien démarrer le projet AFH](#voici-ci-dessous-les-instructions-pour-bien-démarrer-le-projet-afh)
   1. [Création de l'environnement virtuel](#1-création-de-lenvironnement-virtuel)
   2. [Activation de l'environnement virtuel](#2-activation-de-lenvironnement-virtuel)
   3. [Installation des dépendances](#3-instalation-des-dépendances-ou-paquets-dans-lenvironnement-virtuel)
   4. [Navigation dans le dossier backend](#4-navigation-dans-le-dossier-backend)
   5. [Démarrage du serveur backend](#5-démarage-du-serveur-backend)
   6. [Migration des données de la base de données](#6-migrer-les-données-de-la-base-de-données)
4. [Structure du projet](#structure-du-projet)
5. [Prérequis](./requirements.txt)
6. [Docker](#docker)
7. [Tests unitaires](#tests-unitaires)
8. [Documentation API](#documentation-api)
9. [Contributions](#contributions)

---

# Voici les objectifs primordiaux de ce projet :

- Faire la veille sur les modèles et méthodes existants pour le diagnostic de la fertilité masculine
- Analyser et nettoyer cette base de données (photos et données cliniques)
- Proposer un modèle d'IA entraîné pour détecter les hommes ayant un problème de fertilité
- Proposer un protocole de diagnostic pour que le client puisse utiliser votre modèle
- Présenter le modèle au client ainsi que la procédure utilisée pour faire un diagnostic.

## Livrables attendus

- Application en ligne
- Versionné sous GitHub (incluant modèle entraîné, le notebook)
- Code documenté (incluant procédure d'installation nouveau poste dev, procédure d'entraînement du modèle, protocole d'utilisation de l'application)
- Application dockerisé pour le développement
- Route définit en API REST et testé unitairement
- Un trello de la plannification de votre développement, des screenshots périodique de l'état de votre trello

---

# Voici ci-dessous les instructions pour bien démarrer le projet AFH

Ces dernières vont vous permettre de créer un environnement virtuel, y installer les bonnes dépendances, le faire fonctionner et aussi utiliser un conteneur Docker

### **1. Création de l'environnement virtuel**

Ce dernier ira contenir toutes nos dépendances (Paquets)\
Utiliser la commande suivante dans votre terminal (Powershell) :

```sh
python -m venv ./venv
```

---

### **2. Activation de l'environnement virtuel**

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

### **3. Instalation des dépendances (Ou paquets) dans l'environnement virtuel**

```sh
pip install -r requirements.txt
```

---

### **4. Navigation dans le dossier backend**

```sh
cd .\backend\
```

---

### **5. Démarage du serveur backend**

```sh
py manage.py runserver
```

---

### **6. Migrer les données de la base de données**

```sh
py manage.py migrate
```

---
