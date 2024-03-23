import json
from datetime import datetime

from app import JSON_FILE


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