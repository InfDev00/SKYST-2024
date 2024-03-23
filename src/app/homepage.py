from flask import render_template, session, redirect, url_for

from app import app, socketio, POSTS_DATA, USERS_DATA
from app.data import load_data, get_posts, get_user


@app.route('/')
def index():
    if 'user_id' in session:
        posts = get_posts(session['user_id'])
        return render_template('index.html', username=get_user(session['user_id'])['username'], posts=posts)
    else:
        return redirect(url_for('login'))

@socketio.on('request_json')
def send_json():
    data = load_data(POSTS_DATA)
    socketio.emit('json_data', data)