# web_server.py

from http.server import SimpleHTTPRequestHandler, HTTPServer


def run_server(port):
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server(8000)
