from http.server import BaseHTTPRequestHandler, HTTPServer

host = "127.0.0.1"
port = 8008


class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(str({"hello": "world", "id": 12}), "utf-8"))


server = HTTPServer((host, port), SimpleServer)
print(f"Server started at http://{host}:{port} :)")

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()
