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
4. [1er dataset](#dataset-human-sperm-head-morphology-dataset-hushem)
5. [2eme dataset](#dataset---fertility)
6. [Prérequis](./requirements.txt)
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

## Dataset Human Sperm Head Morphology dataset (HuSHeM)

Le dataset "Human Sperm Head Morphology dataset (HuSHeM)" est composé de quatre dossiers, chacun contenant des images de têtes de spermatozoïdes classées selon leur morphologie. Voici un résumé des informations clés :

- **Dossiers :**

  **1. Normal :** Contient environ 50 images de têtes de spermatozoïdes avec une morphologie normale.\
  **2. Tapered :** Contient environ 50 images de têtes de spermatozoïdes de morphologie conique (Tapered).\
  **3. Pyriform :** Contient environ 50 images de têtes de spermatozoïdes de morphologie piriforme (Pyriform).\
  **4. Amorphous :** Contient environ 50 images de têtes de spermatozoïdes de morphologie amorphe (Amorphous).

- **Format des images :** RGB
- **Résolution des images** : 131x131 pixels

Ces images serviront à entraîner notre modèle d'intelligence artificielle pour détecter la morphologie anormale des têtes de spermatozoïdes et ainsi aider à diagnostiquer les problèmes de fertilité masculine.

## Dataset - Fertility

Le fichier CSV "fertility" contient des informations cliniques liées à la fertilité masculine pour chaque individu de l'étude. Voici un résumé des colonnes et des informations qu'elles contiennent :

- **Colonnes du csv :**

  **1. Season :** Saison durant laquelle l'analyse a été effectuée (printemps, automne, etc.).\
  **2. Age :** Âge de l'individu au moment de l'analyse.\
  **3. Childish diseases :** Indique si l'individu a eu des maladies infantiles (oui/non).\
  **4. Accident or serious trauma :** Indique si l'individu a subi un accident ou un traumatisme grave (oui/non).\
  **5. Surgical intervention :** Indique si l'individu a subi une intervention chirurgicale (oui/non).\
  **6. High fevers in the last year :** Indique la fréquence des hautes fièvres dans l'année précédente (jamais, moins de 3 mois auparavant, plus de 3 mois auparavant).\
  **7. Frequency of alcohol consumption :** Fréquence de consommation d'alcool (jamais, occasionnelle, une fois par semaine, plusieurs fois par semaine, plusieurs fois par jour).\
  **8. Smoking habit :** Habitude de fumer (jamais, occasionnelle, quotidienne).\
  **9. Number of hours spent sitting per day :** Nombre d'heures passées assis par jour.\
  **10. Diagnosis :** Diagnostic de fertilité (Normal/Altered).

Ces informations cliniques seront utilisées en conjonction avec les images du premier dataset pour entraîner notre modèle d'intelligence artificielle et détecter les problèmes de fertilité masculine en fonction de la morphologie des têtes de spermatozoïdes.

Pour en savoir plus sur la procédure d'utilisation du dataset et son intégration dans notre modèle, veuillez consulter la section [Instructions pour bien démarrer le projet AFH](#voici-ci-dessous-les-instructions-pour-bien-démarrer-le-projet-afh) dans ce README.
