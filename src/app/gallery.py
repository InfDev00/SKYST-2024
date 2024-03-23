from app import app
from app.data import get_comments, get_post, add_comment, create_post, get_posts, get_user
from flask import request, session, jsonify
import random

@app.route('/api/posts')
def all_posts():
    posts = []
    ids = []
    user_bands = get_user(session['user_id'])['bands']
    for band in user_bands:
        for id in band['member']:
            ids.append(id)
    ids = list(set(ids))
    sample_ids = random.sample(ids, k=len(ids)//2)

    for id in sample_ids:
        posts.extend(get_posts(id))

    return jsonify({
        'result': "ok",
        'session': session,
        'posts': posts
    })


@app.route('/api/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = get_post(post_id)
    if request.method == 'POST':
        content = request.form['content']
        add_comment(get_user(session['user_id'])['username'], post_id, content)
        return jsonify({
            "result": "ok"
        })
    comments = get_comments(post_id)
    return jsonify({
        "result": "ok",
        "post": post,
        "comments": comments
    })


@app.route('/api/create', methods=['POST'])
def create():
    title = request.form['title']
    content = request.form['content']
    create_post(title, session['user_id'], content)
    return jsonify({
        'result': 'ok',
        'redirect': '/'
    })
