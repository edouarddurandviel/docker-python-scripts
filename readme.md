### Créer un env. python sur la base du .toml  existant

```bash
poetry install
```

### Installation de MariaDB
 ```bash

# installation et 
# importation de la base de données
docker compose up -d
```

### smtp4dev
Installation de smtp4dev sur Docker
via le lien: **https://hub.docker.com/r/rnwood/smtp4dev**
En bas à droite lancer la commade: **Run in Docker Desktop**

ou directement en ligne de commande:

```bash
docker pull rnwood/smtp4dev:prerelease
```
> Ne pas oublier de lancer dans Docker Descktop smtp4dev. [localhost:3000](https://localhost:3000 "smtp mails").


---------------------------
## Script de test

### Send extraction report script
```bash
python _send_report_extraction.py
```

```bash
python _load_from_placeholder_to_csv.py
```
Une erreur sera générée, car aucune table n'a été prévue pour recevoir les données de JSONPlaceholder.
Seules la requête HTTP permettant d'appeler JSONPlaceholder et la fonction de création du fichier CSV seront exécutées.  

---------------------------

### poetry add modules

```bash
poetry add <module>
```

### black format

```bash
black <file_name>
```