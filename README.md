# Floupics - TEAM C

Contexte du projet

Le client Floupics vous demande de porter (et améliorer si possible) la base de données réalisée dans l'étape précédente du format SQLite3 au format PostgreSQL

---

La prestation comprend :

- Analyse MCD :
Le premier fichier est le suivi commenté de la modélisation de notre base de données. Il nous a paru pertinent d'expliciter clairement les associations, la multiplicité, et la gestion des clés primaires et étrangères avant de passer à la phase de création de la base de données et à l'insertion des données. Nous vous invitons à explorer ce document en premier lieu, accessible sous le nom de 01-Analyse-MCD.ipynb

- La mise en place de la base de données en Python
La voie du Python --> Le déroulement de la méthode est expliquée dans le fichier `03-Methode2-nb_full_python.ipynb` 
    1. Ouverture de la connexion
    2. Création des tables & insertion des données contenues dans les CSV
    3. Traitements sur les données pour l'ajout des colonnes year & title_only
Les différentes fonctions utilisées pour réaliser les opérations sont contenus dans les deux fichiers suivants:
- utils.py : contient les méthodes qui permettent de travailler à partir des csv et transformer les données. Ici seulement deux des fonctions sont utilisées :

--> list_csv_dict, renvoyer_annee_titre_film)

- crud.py : contient les méthodes qui correspondent aux traitements sur la base de donnée (ouvrir_connection, create_and_insert, lire_donnee, update_database)

- La mise en place de la base de données selon des requêtes SQL
Fichier 2 ParamsBDD : la solution proposée permet de combiner à nouveau du langage SQL au code python et donc on gère dans PostgreSQL la création des nouvelles colonnes et l'alimentation de ces colonnes. On ne sollicite pas de la mémoire vive en plus pour stocker des listes temporairement comme avec la solution 2. L'intégrité des données est aussi respectée.

---

Le dossier comprend :

- 01-Analyse-MCD.ipynb : Analyse 
- 02-ParamsBDD_pgsql.ipynb : projet en SQL
- 03-Methode2-nb_full_python.ipynb : projet en Python
- crud.py
- utils.py
- 1 dossier avec les CSV
- 1 dossier avec les images

---

Ces documents seront disponibles sur GitHub à cette adresse :

https://github.com/Nanogath/Movie2-Groupe-C 


Logiciels utlisés (Download links) :

* [Git](https://gitforwindows.org/)
* [DBeaver](https://dbeaver.io/download/) 
* [PostgreSql](https://www.postgresql.org/download/) 
* [Guide Installation PostGres](https://www.veremes.com/installation-postgresql-windows) 
