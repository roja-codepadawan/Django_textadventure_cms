# Python-Basisimage
FROM python:3.11-slim

# Arbeitsverzeichnis
WORKDIR /app

# Abhängigkeiten kopieren
COPY requirements.txt .

# Abhängigkeiten installieren
RUN pip install --no-cache-dir -r requirements.txt

# Projektdateien kopieren
COPY . .

# Port
EXPOSE 8000

# Startbefehl
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
