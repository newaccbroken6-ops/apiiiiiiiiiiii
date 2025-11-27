from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Serve the index.html file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve static files (if any)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    print("Starting web server for Free Fire Emote Bot...")
    print("Access the interface at: http://localhost:8000")
    app.run(host='0.0.0.0', port=8000, debug=True)