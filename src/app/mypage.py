from app import app
from app.data import get_user
from flask import session, jsonify


@app.route('/api/mypage')
def mypage():
    if 'user_id' not in session:
        return jsonify({
            'result': 'fail',
            'redirect': '/'
        })
    user = get_user(session['user_id'])
    return jsonify({
        'result': 'ok',
        'user': user
    })