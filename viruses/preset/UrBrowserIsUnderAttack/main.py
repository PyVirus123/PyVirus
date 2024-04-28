import os
import webbrowser
import http.server
import socketserver

def start_http_server(port=8000):
    # Get the current directory
    current_dir = os.getcwd()

    # Change to the current directory
    os.chdir(current_dir)

    # Define the Handler class
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=current_dir, **kwargs)

    # Start the HTTP server
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("Serving at port", port)
        try:
            # Open the browser to the server address
            webbrowser.open_new_tab(f"http://localhost:{port}")
            # Serve continuously until interrupted
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    start_http_server()
