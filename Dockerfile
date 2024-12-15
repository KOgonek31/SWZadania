# Używamy oficjalnego obrazu Pythona jako podstawy
FROM python:3.10-slim

# Ustawiamy zmienną PORT (domyślnie 8080, można nadpisać przy uruchamianiu)
ENV PORT=8080

# Tworzymy katalog aplikacji
WORKDIR /app

# Kopiujemy plik serwera do kontenera
COPY server.py /app/server.py

# Instalujemy wymagane pakiety (jeśli potrzebne)
# RUN pip install -r requirements.txt

# Określamy, na jakim porcie serwer nasłuchuje
EXPOSE $PORT

# Definiujemy polecenie uruchamiające serwer
CMD ["python", "server.py"]