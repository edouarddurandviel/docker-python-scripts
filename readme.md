### Créer un env. python sur la base du .toml  existant

```bash
poetry install
```

### Installation de MariaDB
 ```bash

# installtion et import de la base de données
docker compose up -d
```

### smtp4dev
Installation smtp4dev sur Docker
via le lien: **https://hub.docker.com/r/rnwood/smtp4dev**
En bas à droite lancer la commade: **Run in Docker Desktop**

ou directement en ligne de commande:

```bash
docker pull rnwood/smtp4dev:prerelease
```

---------------------------
## Script de test

### Send extraction report script
```bash
python _send_report_extraction.py
```

---------------------------

### poetry add modules

```bash
poetry add <module>
```

### black format

```bash
black <file_name>
```