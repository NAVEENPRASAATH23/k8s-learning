# pyrefly: ignore [missing-import]
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    message = "Hi This is the Webapp running on Nodeport IP in pod for the testing purpose"
    return f"<h1>{message}</h1>\n<p>Pod ID: {os.environ.get('HOSTNAME', 'localhost')}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
