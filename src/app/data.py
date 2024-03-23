import json
from datetime import datetime
from werkzeug.security import check_password_hash

from app import POSTS_DATA, USERS_DATA

# default function
def load_data(key):
    try:
        with open(key, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        if key==POSTS_DATA:
            data = {"posts": [], "comments": []}
        elif key==USERS_DATA:
            data = {}
    return data

def save_data(data, key):
    with open(key, 'w') as file:
        json.dump(data, file, indent=4)

# gallery function
def create_post(title, user_id, content):
    data = load_data()
    new_post = {
        "post_id": len(data["posts"]) + 1,
        "username":get_user(user_id)['username'],
        "user_id":user_id,
        "title": title,
        "content": content,
        "date_posted": datetime.utcnow().isoformat(),
        "comments": []
    }
    data["posts"].append(new_post)
    save_data(data,POSTS_DATA)
    return new_post

def add_comment(username, post_id, content):
    data = load_data(POSTS_DATA)

    comment = {
        "num": len(data["comments"]) + 1,
        "username": username,
        "post_id": post_id,
        "content": content,
        "date_commented": datetime.utcnow().isoformat()
    }
    data["comments"].append(comment)
    save_data(data,POSTS_DATA)
    return comment

def get_posts():
    data = load_data(POSTS_DATA)
    return data["posts"]

def get_post(post_id):
    data = load_data(POSTS_DATA)
    for post in data["posts"]:
        if post["id"] == post_id:
            return post
    return None

def get_comments(post_id):
    data = load_data(POSTS_DATA)
    comments = []
    for comment in data["comments"]:
        if comment["post_id"] == post_id:
            comments.append(comment)
    return comments


# login function
def authenticate(username, password):
    users = load_data(USERS_DATA)
    if username in users and check_password_hash(users[username], password):
        return True
    return False

def register_user(username, id, password):
    data = load_data(USERS_DATA)
    #사용자 정보 확인
    for key in data.keys():
        if data[key]["username"] == username:
            return False, "이미 사용 중인 사용자 이름입니다."
        if data[key]["id"] == id:
            return False, "이미 사용 중인 아이디입니다."
        if data[key]["password"] == password:
            return False, "이미 사용 중인 비밀번호입니다."
    
     # 사용자 정보 저장
    new_user = {
        "username": username,
        "id": id,
        "password": password  # 비밀번호 저장 전에 해싱 또는 암호화 필요
    }
    data[id] = new_user
    save_data(data, USERS_DATA)
    
    return True, "회원가입이 완료되었습니다."

def get_user(id):
    users = load_data(USERS_DATA)
    return users.get(id)