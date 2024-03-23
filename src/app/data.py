import json
from datetime import datetime
from werkzeug.security import check_password_hash

from app import JSON_FILE, USERS_FILE


def load_data(key):
    try:
        with open(key, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        if key==JSON_FILE:
            data = {"posts": [], "comments": []}
        elif key==USERS_FILE:
            data = {}
    return data

def save_data(data, key):
    with open(key, 'w') as file:
        json.dump(data, file, indent=4)

# JSON_FILE 관련 함수
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
    save_data(data,JSON_FILE)
    return new_post

def add_comment(post_id, content):
    data = load_data(JSON_FILE)
    comment = {
        "id": len(data["comments"]) + 1,
        "post_id": post_id,
        "content": content,
        "date_commented": datetime.utcnow().isoformat()
    }
    data["comments"].append(comment)
    save_data(data,JSON_FILE)
    return comment

def get_posts():
    data = load_data(JSON_FILE)
    return data["posts"]

def get_post(post_id):
    data = load_data(JSON_FILE)
    for post in data["posts"]:
        if post["id"] == post_id:
            return post
    return None

def get_comments(post_id):
    data = load_data(JSON_FILE)
    comments = []
    for comment in data["comments"]:
        if comment["post_id"] == post_id:
            comments.append(comment)
    return comments


# login 관련 함수
def authenticate(username, password):
    users = load_data(USERS_FILE)
    if username in users and check_password_hash(users[username], password):
        return True
    return False