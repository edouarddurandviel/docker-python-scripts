### Create python venv from existing .toml

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