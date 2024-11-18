This project is made for my university assignment.
Every task contains a separate branch and screenshots of completed task.
For this purpose I'm gonna use Flask framework, which requoires python to be installed with a few libraries
listed in the pyproject.toml file.


# Task 5

Enable 2FA in profile page (disable by default).
For these purposes I'm gonna use flask-security library. (see [References](#references-and-additional-information)

- [ ] 2FA

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

# Configuration

Create *.env* file in src/app folder if you haven't already.

Example:
```
SECRET_KEY="" # for csrf protection
SQLALCHEMY_DATABASE_URI = "" # link to the database
MAIL_DEFAULT_SENDER = "" # default sender email
MAIL_PASSWORD = "" # password to this email
```

# References and additional information

1. [Docker official documentation - Docker](https://docs.docker.com)
2. [Bcrypt - Wiki](https://en.wikipedia.org/wiki/Bcrypt)
3. [Colors for the app](https://coolors.co/palette/f94144-f3722c-f8961e-f9c74f-90be6d-43aa8b-577590)
4. [WTForms official docs](https://wtforms.readthedocs.io/en/)
5. [Flask Simple Captcha docs](https://pypi.org/project/flask-simple-captcha/)
6. [Flask Mail docs](https://flask-mail.readthedocs.io)
7. [How to send an e-mail with Flask and Flask-Mail? - Medium](https://medium.com/@lewis.devs/how-to-send-an-e-mail-with-flask-a13e751a5cab)
8. [Flask-security docs](https://flask-security-too.readthedocs.io)