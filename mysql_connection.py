from http.server import HTTPServer, BaseHTTPRequestHandler
from functions import introduction  # Import from intro.py

class WebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        content = introduction()  # Call the function to get the HTML
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

# Run the server
server_address = ('', 8000)
httpd = HTTPServer(server_address, WebHandler)

print("Server running at http://localhost:8000/")
httpd.serve_forever()