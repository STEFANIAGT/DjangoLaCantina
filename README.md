# DjangoLaCantina
Applicazione Django per la gestione, visualizzazione e valutazione dei vini.

# Overview
DjangoLaCantina è un progetto web basato su Django 5 che permette di:

gestire una collezione di vini

visualizzare liste, dettagli e classifiche

importare dati

votare i vini

utilizzare template HTML personalizzati e CSS dedicato

Stack Tecnologico
Python 3.12

Django 5.x

SQLite (default)

HTML / CSS (template + static)

# Struttura del Progetto
...
Codice
DjangoLaCantina/
│
|
├── DjangoLaCantina/   # Configurazione principale (settings, urls, wsgi, asgi)
├── core/              # App principale: modelli, viste, form, template
├── static/            # CSS, immagini
├── templates/         # Template globali
├── manage.py
└── db.sqlite3
Avvio del Progetto
bash
git clone https://github.com/STEFANIAGT/DjangoLaCantina.git
cd DjangoLaCantina

python -m venv venv
venv\Scripts\activate   # Windows

pip install django
python manage.py runserver
Apri nel browser:
http://127.0.0.1:8000/ (127.0.0.1 in Bing)

Funzionalità Principali
CRUD vini

Lista vini e dettaglio

Template dedicati (wine_list, vote, import, ecc.)

Sistema di voto

Migrazioni già configurate



 Note
Il repository contiene solo i file essenziali del progetto Django.
L’ambiente virtuale è escluso tramite .gitignore.
