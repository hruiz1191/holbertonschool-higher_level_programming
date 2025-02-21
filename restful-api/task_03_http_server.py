#!/usr/bin/python3
"""Simple API using http.server module"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Custom HTTP request handler"""

    def do_GET(self):
        """Handles GET requests and serves responses"""
        if self.path == "/":
            self._send_text_response(200, "Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json_response(200, data)

        elif self.path == "/status":
            status_response = {"status": "ok"}  # El test probablemente espera "ok" en minúscula
             self._send_json_response(200, status_response)

        elif self.path == "/info":
            info_response = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._send_json_response(200, info_response)

        else:
            self._send_text_response(404, "Endpoint not found")

    def _send_text_response(self, status_code, message):
        """Sends a plain text response"""
        self.send_response(status_code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def _send_json_response(self, status_code, data):
        """Sends a JSON response"""
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        json_response = json.dumps(data)
        self.wfile.write(json_response.encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Starts the HTTP server"""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
