# Krzysztof Ogonek
# Używamy oficjalnego obrazu Pythona jako podstawy
FROM python:3.10-slim

# Ustawiamy zmienną PORT
ENV PORT=8081

# Tworzymy katalog aplikacji
WORKDIR /app

# Kopiujemy plik serwera do kontenera
COPY server.py /app/server.py

# Określamy, na jakim porcie serwer nasłuchuje
EXPOSE $PORT

# Definiujemy polecenie uruchamiające serwer
CMD ["python", "server.py"]
