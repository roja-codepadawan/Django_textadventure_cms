# Django_textadventure_cms

# TextAdventure CMS

Ein webbasiertes Content-Management-System für interaktive Textadventures, entwickelt mit Django und Docker.

## Features

* Verwaltung von Geschichten (Stories), Kapiteln, Entscheidungen und Variablen
* Admin-Interface für Content-Erstellung
* SQLite-Datenbank
* Docker-basierte Entwicklungsumgebung
* Spiel-Frontend in Vorbereitung

---

## Projektstruktur

```
textadventure_cms/
├── cms/                  # Haupt-App für Story-Management
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── textadventure_cms/   # Django-Konfiguration
│   └── urls.py
├── manage.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Setup-Anleitung

### 1. Projekt klonen / erstellen

```bash
mkdir textadventure_cms && cd textadventure_cms
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install django
django-admin startproject textadventure_cms .
python manage.py startapp cms
```

### 2. Docker Setup

 **Dockerfile** :

```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

 **docker-compose.yml** :

```yaml
services:
  web:
    build: .
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1
```

 **requirements.txt** :

```txt
Django>=4.2
```

### 3. Migrationen & Superuser

```bash
docker compose run web python manage.py makemigrations
docker compose run web python manage.py migrate
docker compose run web python manage.py createsuperuser
docker compose up
```

Rufe dann im Browser auf:** **[http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## Verwendete Modelle (`cms/models.py`)

* `Story`: Titel + Beschreibung
* `Chapter`: Textinhalt + Start-Marker + Verknüpfung zur Story
* `Choice`: Entscheidung zwischen Kapiteln mit optionaler Bedingung/Wirkung
* `Variable`: Story-Variablen mit Default-Werten

---

## Nächste Schritte

### ✅ Spiel-Frontend (Basis)

* ✓ Startkapitel anzeigen
* ✓ Entscheidungen mit Links zu nächsten Kapiteln
* ✓ Story-Verlauf aus Datenbank lesen

### ✨ Geplant: Story-Builder-Tool

* ✓ Drag & Drop Kapitelstruktur
* ✓ Visualisierung des Story-Baums
* ✓ Direktes Bearbeiten von Inhalten & Verzweigungen (HTMX/React)

---

## Wichtige Befehle

| Aktion                | Befehl                                                      |
| --------------------- | ----------------------------------------------------------- |
| Migrationen erstellen | `docker compose run web python manage.py makemigrations`  |
| Migrationen anwenden  | `docker compose run web python manage.py migrate`         |
| Superuser erstellen   | `docker compose run web python manage.py createsuperuser` |
| Container starten     | `docker compose up`                                       |
| Django Shell öffnen  | `docker compose run web python manage.py shell`           |

---

## Lizenz

MIT License

---

Für Feedback oder Erweiterungen gerne melden :)
