from flask import render_template, request, redirect, url_for

from app import app
from app.data import get_comments, get_post, add_comment, create_post


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = get_post(post_id)
    if request.method == 'POST':
        content = request.form['content']
        add_comment(post_id, content)
        return redirect(url_for('post', post_id=post_id))
    comments = get_comments(post_id)
    return render_template('post.html', post=post, comments=comments)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        create_post(title, content)
        return redirect('/')
    return render_template('create.html')