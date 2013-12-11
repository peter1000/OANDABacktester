import http.server
import socketserver

PORT = 80

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("localhost", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()