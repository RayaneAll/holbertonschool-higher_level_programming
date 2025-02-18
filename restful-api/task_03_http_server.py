#!/usr/bin/env python3
"""A simple HTTP server that responds to GET requests with JSON data."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Gère les requêtes GET et renvoie des réponses appropriées"""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_json({"name": "John", "age": 30, "city": "New York"})

        elif self.path == "/status":
            self.send_json({"status": "OK"})

        elif self.path == "/info":
            self.send_json({
                "version": "1.0",
                "description": "A simple API built with http.server"
            })

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = json.dumps(
                {"error": "Endpoint not found"}
            ).encode("utf-8")
            self.wfile.write(error_message)

    def send_json(self, data):
        """Envoie une réponse JSON au client"""
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = json.dumps(data).encode("utf-8")
        self.wfile.write(response)


def run(server_class=HTTPServer,
        handler_class=SimpleHTTPRequestHandler,
        port=8000):
    """Lance le serveur HTTP sur le port spécifié"""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
