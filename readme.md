### Create python venv
```bash
python3 -m venv project-env
```

### Install modules
```bash
poetry install
```

### MariaDB installation
 ```bash

# will import existing database
docker compose up -d
```

### smtp4dev
Primarily, open docker desktop, then
follow link: **https://hub.docker.com/r/rnwood/smtp4dev**
finally, down to the bottom right, right click on **Run in Docker Desktop**

or do the command:

```bash
docker pull rnwood/smtp4dev:prerelease
```

---------------------------

### run script with poetry

```bash
poetry run python main.py
```

### poetry add modules

```bash
poetry add <module>
```

### black format

```bash
black <file_name>
```