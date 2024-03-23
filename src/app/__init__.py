from flask import Flask
from flask_cors import CORS
import os


app = Flask(__name__)
app.config['SECRET_KEY'] =  os.urandom(24)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
POSTS_DATA = "posts.json"
USERS_DATA = 'users.json'


from app import login, gallery, homepage, mypage
