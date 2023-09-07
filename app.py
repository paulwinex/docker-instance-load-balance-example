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



# from fastapi import FastAPI
# import uvicorn
# import random
#
# MY_NUM = random.randint(1, 100)
#
# app = FastAPI()
#
#
# @app.get('/')
# async def index():
#     print(MY_NUM)
#     return {"message": MY_NUM}
#
#
# if __name__ == '__main__':
#     uvicorn.run('app:app', host='0.0.0.0', port=5000, reload=True)
