import http.server
import socketserver
from random import randint

PORT = 5000
MY_NUMBER = randint(1, 100)


class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            print(f'{MY_NUMBER=}', flush=True)
            self.wfile.write(f"<h1>{MY_NUMBER}</h1>".encode())
        else:
            self.send_response(404)
            self.end_headers()


with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()
