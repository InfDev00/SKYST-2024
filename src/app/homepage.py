from app import app
from app.data import get_posts
from flask import session, jsonify


@app.route('/')
def index():
    if 'user_id' in session:
        posts = get_posts(session['user_id'])
        # return render_template('index.html', username=get_user(session['user_id'])['username'], posts=posts)
        response = {
            "result": "ok"
        }
        return jsonify(response)
    else:
        response = {
            "result": "fail",
            "redirect": "/login"
        }
        return jsonify(response)
