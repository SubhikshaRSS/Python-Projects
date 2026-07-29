#http_post_service.py
from http.server import BaseHTTPRequestHandler, HTTPServer
class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers["Content-Length"])
        data = self.rfile.read(length)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST request received")
        print(data.decode())
server = HTTPServer(("localhost", 8000), MyHandler)
print("Server running on http://localhost:8000")
server.serve_forever()
