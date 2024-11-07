This project is made for my university assignment.
Every task contains a separate branch and screenshots of completed task.
For this purpose I'm gonna use Flask framework, which requoires python to be installed with a few libraries
listed in the pyproject.toml file.

# Installation

The app can be launched manually and through docker container.
First step is to clone git repo:

Using HTTPS
```bash
git clone https://github.com/LostHopes/secured-accounts-lab.git secure-accounts
```

or SSH
```bash
git clone https://github.com/LostHopes/secured-accounts-lab.git secure-accounts
```

## Manual installation

Create python virtual environment
```bash
python -m venv .env
```

Activate python virtual environment
```bash
source .env/bin/activate
```

Install packages
```bash
pip install --upgrade pip
pip install poetry
poetry install
```
Launch an app
```bash
python src/app.py
```

## Installation using Docker

Build an image from a Dockerfile
```bash
sudo docker built -t sucure-accounts .
```

Run a container
```bash
sudo docker run -p 5000:5000 secure-accounts
```

# References and additional information

1. [Docker official documentation](https://docs.docker.com)