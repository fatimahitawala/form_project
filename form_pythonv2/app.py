import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

DB_NAME = "/app/data/formdata.db"

# Create table
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS submissions (name TEXT, email TEXT)''')
conn.commit()
conn.close()

class SimpleFormHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"""
            <html><body>
            <h2>Submit your details</h2>
            <form method="post">
              Name: <input name="name" required><br><br>
              Email: <input name="email" type="email" required><br><br>
              <input type="submit">
            </form>
            </body></html>
        """)

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_data = self.rfile.read(content_len).decode()
        fields = urllib.parse.parse_qs(post_data)
        name = fields.get("name", [""])[0]
        email = fields.get("email", [""])[0]

        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("INSERT INTO submissions VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()

        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(('', 80), SimpleFormHandler)
    print("Server running at http://localhost")
    server.serve_forever()
