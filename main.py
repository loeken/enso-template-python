from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    port = os.getenv("PORT")
    print(f"Server listening on port {port}")
    app.run(host='0.0.0.0', port=port)