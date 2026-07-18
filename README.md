# 📦 Eco-Stock API

## Présentation

Eco-Stock est une API REST développée avec **Django** et **Django REST Framework**. Elle permet de gérer les entrepôts de stockage ainsi que les produits alimentaires destinés à être redistribués avant leur date de péremption.

L'API offre les fonctionnalités suivantes :

- Gestion des entrepôts
- Gestion des produits
- Transfert d'un produit entre deux entrepôts
- Audit d'un entrepôt
- Authentification sécurisée avec JWT

---

# Architecture du projet

L'application repose sur deux modèles principaux.

## Warehouse

Représente un entrepôt.

| Champ        | Description |
|--------      |-------------|
| nom          | Nom de l'entrepôt |
| localisation | Adresse ou zone géographique |
| capacite     | Nombre maximal de produits pouvant être stockés |

---

## Product

Représente un produit alimentaire.

| Champ           | Description |
|--------         |-------------|
| nom             | Nom du produit |
| quantite        | Quantité disponible |
| date_expiration | Date limite de consommation |
| etat            | disponible, réservé ou périmé |
| warehouse       | Entrepôt auquel appartient le produit |

Chaque produit appartient à **un seul entrepôt**, tandis qu'un entrepôt peut contenir **plusieurs produits** (relation One-To-Many).

---

# Installation du projet

Cette section explique comment installer le projet sur une nouvelle machine.

## 1. Cloner le dépôt

```bash
git clone https://github.com/votre-compte/eco-stock.git

cd eco-stock
```

### Pourquoi ?

Cette commande télécharge le projet depuis GitHub et permet d'accéder à son dossier.

---

## 2. Créer un environnement virtuel

```bash
python -m venv venv
```

### Pourquoi ?

L'environnement virtuel isole les dépendances du projet afin qu'elles n'interfèrent pas avec celles des autres projets Python installés sur la machine.

---

## 3. Activer l'environnement virtuel

### Sous Linux / macOS

```bash
source venv/bin/activate
```

### Sous Windows

```bash
venv\Scripts\activate
```

### Pourquoi ?

Une fois activé, toutes les bibliothèques Python seront installées uniquement dans cet environnement.

---

## 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

### Pourquoi ?

Le fichier `requirements.txt` contient toutes les bibliothèques nécessaires au fonctionnement du projet (Django, DRF, Simple JWT, etc.).

Cette commande les installe automatiquement.

---

## 5. Appliquer les migrations

```bash
python manage.py migrate
```

### Pourquoi ?

Cette commande crée les tables de la base de données à partir des modèles Django.

---

## 6. Lancer le serveur

```bash
python manage.py runserver
```

### Pourquoi ?

Cette commande démarre le serveur de développement.

L'API devient alors accessible depuis le navigateur ou un client comme Postman.

---

# Authentification

L'API est protégée grâce à **JWT (JSON Web Token)**.

Seuls les utilisateurs authentifiés peuvent créer, modifier ou supprimer des données.

Pour chaque requête protégée, le token doit être envoyé dans l'en-tête :

```http
Authorization: Bearer votre_access_token
```

---

# Documentation OpenAPI

La documentation interactive est générée automatiquement grâce à **drf-spectacular**.

Elle permet :

- de consulter tous les endpoints ;
- de visualiser les paramètres attendus ;
- de tester directement les requêtes depuis le navigateur.

### Swagger UI

```
http://127.0.0.1:8000/api/schema/swagger-ui/
```

### ReDoc

```
http://127.0.0.1:8000/api/schema/redoc/
```

### Schéma OpenAPI

```
http://127.0.0.1:8000/api/schema/
```

---

# Endpoints

## Authentification

| Méthode     | Endpoint             | Description |
|----------   |----------            |-------------|
| POST        | /api/token/          | Obtenir un token JWT |
| POST        | /api/token/refresh/  | Renouveler un token |

---

## Warehouses

| Méthode        | Endpoint               | Description |
|----------      |----------              |-------------|
| GET            | /api/warehouses/       | Liste des entrepôts |
| GET            | /api/warehouses/{id}/  | Détails d'un entrepôt |
| POST           | /api/warehouses/       | Créer un entrepôt |
| PUT            | /api/warehouses/{id}/  | Modifier un entrepôt |
| PATCH          | /api/warehouses/{id}/  | Modifier partiellement |
| DELETE         | /api/warehouses/{id}/  | Supprimer un entrepôt |

---

## Audit

```
GET /api/warehouses/{id}/audit/
```

### Description

Retourne un résumé de l'entrepôt.

Exemple :

- capacité
- nombre total de produits
- nombre de produits disponibles
- nombre de produits réservés
- nombre de produits périmés

Cette fonctionnalité est implémentée avec `@action(detail=True)`.

---

## Produits

| Méthode         | Endpoint             | Description |
|----------       |----------            |-------------|
| GET             | /api/products/       | Liste des produits |
| GET             | /api/products/{id}/  | Détails d'un produit |
| POST            | /api/products/       | Ajouter un produit |
| PUT             | /api/products/{id}/  | Modifier un produit |
| PATCH           | /api/products/{id}/  | Modifier partiellement |
| DELETE          | /api/products/{id}/  | Supprimer un produit |

---

## Transfert

```
POST /api/products/{id}/move/
```

### Description

Permet de déplacer un produit vers un autre entrepôt.

Le transfert est refusé si le produit est déjà périmé.

Cette fonctionnalité est implémentée avec `@action(detail=True)`.

---

# Sécurité

Les permissions sont configurées de la manière suivante :

| Action                | Authentification |
|--------               |------------------|
| Consulter les données | Non|
| Ajouter un produit    | Oui |
| Modifier un produit   | Oui |
| Supprimer un produit  | Oui |
| Transférer un produit | Oui |
| Effectuer un audit    | Oui |

---

# Technologies utilisées

- Python 3
- Django
- Django REST Framework
- Simple JWT
- drf-spectacular (OpenAPI)
- SQLite 

---

# Auteur

Projet réalisé dans le cadre du développement d'une API REST pour la startup **Eco-Stock**.
