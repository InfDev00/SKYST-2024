from app import app
from app.data import authenticate, register_user, get_user
from flask import request, session, jsonify


@app.route('/api/register', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    id = request.form['id']

    is_regist, text = register_user(username, id, password)

    if is_regist:
        response = {
            "result": "ok",
            "redirect": "/login"
        }
        return jsonify(response)

    response = {
        "result": "fail"
    }
    return jsonify(response)


@app.route('/api/login', methods=['POST'])
def login():
    id = request.form['id']
    password = request.form['password']
    if authenticate(id, password):
        session['user_id'] = get_user(id)['id']
        print(session)
        response = {
            "result": "ok",
            "session": session,
            "redirect": "/"
        }
        return jsonify(response)
    else:
        print("err")
        response = {
            "result": "fail"
        }
        return jsonify(response)


@app.route('/api/logout')
def logout():
    session.pop('user_id', None)
    response = {
        "result": "ok",
        "redirect": "/"
    }
    return jsonify(response)
