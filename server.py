from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.path = '/output.html'  # 重新導向根目錄到 output.html
        return super().do_GET()

PORT = 8000

if __name__ == "__main__":
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"✅ Server running at http://127.0.0.1:{PORT}/")
    httpd.serve_forever()
