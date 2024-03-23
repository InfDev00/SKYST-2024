from app import app
from app.data import get_comments, get_post, add_comment, create_post, get_posts, get_user, get_bands, get_band, enter_band, create_band
from flask import request, session, jsonify


@app.route('/api/band')
def all_bands():
    bands = get_bands()
    return jsonify({
        'result': "ok",
        'session': session,
        'bands': bands
    })

@app.route('/api/band/<int:band_id>', methods=['GET'])
def band(band_id):
    band = get_band(band_id)
    return jsonify({
        "result": "ok",
        "band":band
    })

@app.route('/api/band/join/<int:band_id>', methods=['GET'])
def join_band(band_id):
    enter_band(band_id, session["user_id"])

    return jsonify({
        "result": "ok",
    })

@app.route('/api/band/create', methods=['POST'])
def createband():
    bandname = request.form['bandname']
    comment = request.form['comment']

    create_band(bandname, session["user_id"],comment)
    return jsonify({
        'result': 'ok',
        'redirect': '/'
    })