#!/usr/bin/python3
"""Module to implement http.server module"""
import http.server
import json


class HTTPHandler(http.server.BaseHTTPRequestHandler):
    """Simple Handler class inherited from BaseHTTPRequestHandler"""

    def do_GET(self):
        """Method to handle GET requests"""

        # Base case
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Hello, this is a simple API!'.encode())

        # If /data is accessed
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # /status endpoint
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        # /info endpoint (CORREGIDO)
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # Error 404
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')  # ✅ Ahora responde con JSON
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode("utf-8"))


if __name__ == '__main__':
    """Server initialization"""
    server_address = ('', 8000)
    httpserver = http.server.HTTPServer(server_address, HTTPHandler)
    print("Server running on port 8000...")
    httpserver.serve_forever()

