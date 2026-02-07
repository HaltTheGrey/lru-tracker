"""Simple HTTPS server for testing auto-update locally."""
import http.server
import ssl
import os

# Change to the directory containing version_v1.2.0.json
os.chdir(r'c:\Users\jessneug\Leetcode\templeteforpartwalks')

# Create a simple HTTP server
PORT = 8443

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve version_v1.2.0.json as version.json
        if self.path == '/version.json':
            self.path = '/version_v1.2.0.json'
        return super().do_GET()

print(f"Starting HTTPS server on port {PORT}...")
print(f"Update URL will be: https://localhost:{PORT}/version.json")
print("Press Ctrl+C to stop")

httpd = http.server.HTTPServer(('localhost', PORT), MyHTTPRequestHandler)

# For testing, we'll use HTTP instead (simpler)
# In production, always use HTTPS
print("\nWARNING: Using HTTP for local testing only!")
print("Change port to 8000 for HTTP testing")

httpd.serve_forever()
