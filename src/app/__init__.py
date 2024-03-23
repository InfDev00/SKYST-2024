from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
JSON_FILE = "posts.json"
USERS_FILE = 'users.json'
socketio = SocketIO(app)

from app import login, gallery, homepage