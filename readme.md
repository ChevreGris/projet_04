Projet 04 du cursus Python d'OpenClassrooms, 2021.
Ce script à été fait sur mac os, et testé sur windows et mac os.

## Installation

Python3 doit être installé correctement.
Clonner ce projet depuis le dossier code
Depuis la racine du projet, créer un environement virtuel et lancer le script:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 code/mvc/__main__.py
```
## Flake8 html

Pour lancer le rapport flake8 html:

```
pip install flake8-html
flake8 --format=html --htmldir=flake-report
```

Un dossier est créé (flake-report), la rapport ce trouve dedans.

## Usage

Ce script permet de gérer des tournois d'echecs, avec une gestion de joueurs, et une gestion de tournois.