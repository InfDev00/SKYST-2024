from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime

app = Flask(__name__)
JSON_FILE = "posts.json"

def load_data():
    try:
        with open(JSON_FILE, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"posts": [], "comments": []}
    return data

def save_data(data):
    with open(JSON_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def create_post(title, content):
    data = load_data()
    new_post = {
        "id": len(data["posts"]) + 1,
        "title": title,
        "content": content,
        "date_posted": datetime.utcnow().isoformat(),
        "comments": []
    }
    data["posts"].append(new_post)
    save_data(data)
    return new_post

def add_comment(post_id, content):
    data = load_data()
    comment = {
        "id": len(data["comments"]) + 1,
        "post_id": post_id,
        "content": content,
        "date_commented": datetime.utcnow().isoformat()
    }
    data["comments"].append(comment)
    save_data(data)
    return comment

def get_posts():
    data = load_data()
    return data["posts"]

def get_post(post_id):
    data = load_data()
    for post in data["posts"]:
        if post["id"] == post_id:
            return post
    return None

def get_comments(post_id):
    data = load_data()
    comments = []
    for comment in data["comments"]:
        if comment["post_id"] == post_id:
            comments.append(comment)
    return comments

@app.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)

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

if __name__ == "__main__":
    app.run(debug=True)
