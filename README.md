DjangoLaCantina
Applicazione Django per la gestione e valutazione dei vini. Include modelli, viste, template e funzionalità di import/voto.

Tecnologie
Python 3.12

Django 5.x

SQLite (default)

HTML/CSS (template + static)

Struttura
Codice
DjangoLaCantina/
├── DjangoLaCantina/   # Configurazione progetto (settings, urls, wsgi, asgi)
├── core/              # App principale: modelli, viste, form, template
├── static/            # CSS, immagini
├── templates/         # Template globali
├── manage.py
└── db.sqlite3
Funzionalità
CRUD vini

Liste, dettagli, top wines

Import dati

Sistema di voto

Template responsive

Avvio progetto
bash
git clone https://github.com/STEFANIAGT/DjangoLaCantina.git
cd DjangoLaCantina
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py runserver
