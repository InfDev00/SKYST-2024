from flask import Flask
from flask_socketio import SocketIO
import os


app = Flask(__name__)
app.config['SECRET_KEY'] =  os.urandom(24)
POSTS_DATA = "posts.json"
USERS_DATA = 'users.json'
socketio = SocketIO(app)


from app import login, gallery, homepage
