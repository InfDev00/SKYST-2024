from flask import render_template, request, redirect, url_for, session

from app import app
from app.data import get_comments, get_post, add_comment, create_post, get_posts, get_user


@app.route('/post')
def all_posts():
        posts = get_posts(session['user_id'])
        return render_template('index.html', username=get_user(session['user_id'])['username'], posts=posts)

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = get_post(post_id)
    if request.method == 'POST':
        content = request.form['content']
        add_comment(get_user(session['user_id'])['username'], post_id, content)
        return redirect(url_for('post', post_id=post_id))
    comments = get_comments(post_id)
    return render_template('post.html', post=post, comments=comments)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        create_post(title, session['user_id'], content)
        return redirect('/')
    return render_template('create.html')