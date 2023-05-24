
import http.server
import socketserver
import openpyxl
import subprocess

# Set the port number for the web server
PORT = 8000

# Load the Excel file
workbook = openpyxl.load_workbook('IMDB Movie Ratings.xlsx')
sheet = workbook['Top Rated Movies']

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add the 'Access-Control-Allow-Origin' header to allow loading CSS from a different origin
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_GET(self):
        if self.path == "/":
            # Redirect the request to "random_movie.html"
            self.send_response(301)
            self.send_header('Location', '/random_movie.html')
            self.end_headers()
        elif self.path == "/random_movie.html":
            # Run generate_html.py to generate the HTML dynamically
            subprocess.run(['python', 'generate_html.py'])

            # Read the contents of the HTML file
            with open('random_movie.html', 'r') as file:
                html = file.read()

            # Set the response headers
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Send the HTML response
            self.wfile.write(html.encode())
        elif self.path == "/styles.css":
            # Read the contents of the CSS file
            with open('styles.css', 'r') as file:
                css = file.read()

            # Set the response headers
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()

            # Send the CSS response
            self.wfile.write(css.encode())
        else:
            # Call the base class's do_GET method for regular requests
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Start the web server with the custom handler
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Server running on port {PORT}")
    httpd.serve_forever()

