from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import os
from datetime import datetime

AUTHOR_NAME = "Krzysztof Ogonek"

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Pobieramy adres IP klienta
        client_ip = self.client_address[0]
        
        # Przygotowujemy odpowiedź HTML
        response = f"""
        <html>
        <head><title>Adres IP klienta</title></head>
        <body>
        <h1>Twój adres IP to: {client_ip}</h1>
        </body>
        </html>
        """
        
        # Wysyłamy odpowiedź
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
    
    def log_message(self, format, *args):
        return  # Wyłączamy domyślne logowanie HTTPServer

def run():
    port = int(os.getenv('PORT', 8081))
    logging.basicConfig(level=logging.INFO)
    
    # Logowanie szczegółów serwera
    logging.info("Serwer uruchomiony")
    logging.info(f"Autor: {AUTHOR_NAME}")
    logging.info(f"Data uruchomienia: {datetime.now()}")
    logging.info(f"Port TCP: {port}")
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    logging.info("Serwer nasłuchuje...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
