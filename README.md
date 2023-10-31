# Projet de Structuration de la Base de Données Castorama France

## Description

Ce projet est une continuation du travail fourni dans le projet `scrap_projects` (https://github.com/Val832/scrap_projects), et plus précisément sur l'expansion du projet d'extraction du catalogue complet de Castorama France. L'objectif est de transformer une base de données semi-structurée issue de l'extraction du catalogue en une base de données relationnelle en utilisant le module SQLite de Python. Cette étape est essentielle pour optimiser l'intégration, la gestion et l'analyse des données au sein de systèmes de gestion de bases de données relationnelles (SGBDR).

## Processus du Projet

Le projet se développe en trois phases distinctes :

### 1. Conception du Schéma de Base de Données

- Réflexion approfondie et élaboration du schéma de la base de données.
- Le schéma conceptuel est disponible dans le fichier `db_diagram` situé à la racine du projet.

### 2. Création de l'Architecture de la Base de Données

- Mise en place de l'architecture de la base de données en utilisant le module `sqlite3` de Python.
- Les scripts de création des tables sont conçus pour aligner la structure de la base de données sur le schéma établi.

### 3. Alimentation de la Base de Données

- Développement d'une fonction Python pour interpréter le fichier JSON issu de l'extraction des données produits de Castorama France.
- Insertion des données dans la base de données SQLite en respectant les relations et contraintes du schéma.

## Remarques

### Limitation du fichier `data.json`

Pour des raisons de simplicité et afin de faciliter le téléchargement et la manipulation du projet, le fichier `data.json` fourni dans ce projet ne contient qu'un échantillon réduit de 100 produits. Cet échantillon est représentatif de la structure générale des données et permet de tester l'ensemble des fonctionnalités du projet.

