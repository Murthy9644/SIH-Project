
import http.server
import ssl
import os

import sys

# Default port
PORT = 5500

# Check if a port is provided as a command-line argument
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        print("Invalid port number. Using default port 5503.")

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

server_address = ("0.0.0.0", PORT)

httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

try:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(keyfile="key.pem", certfile='cert.pem')
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print(f"Serving HTTPS on port {PORT}")
    print("\n--- IMPORTANT ---")
    print(f"For camera access, open this link in your browser: https://localhost:{PORT}")
    print("Modern browsers require a secure connection (HTTPS) or localhost to access the camera.")
    print(f"You can also use this link on your mobile device: https://192.168.1.6:{PORT}")
    print("If you use the mobile link, you MUST accept the security warning in your browser.")
    print("-----------------")
    httpd.serve_forever()
except FileNotFoundError:
    print("\nERROR: Could not find 'key.pem' or 'cert.pem'.")
    print("Please generate these files first by following the instructions.")
except Exception as e:
    print(f"An error occurred: {e}")

