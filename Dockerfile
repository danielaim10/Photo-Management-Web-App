FROM python:3.9-slim

# Setează directorul de lucru
WORKDIR /app

# Copiază fișierele din directorul curent în directorul /app din imagine
COPY . .

# Instalează pachetele necesare
RUN pip install --no-cache-dir -r requirements.txt

# Exposează portul 5000
EXPOSE 5000

# Comanda de pornire a aplicației
CMD ["python3", "app.py"]