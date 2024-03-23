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

def register_user(username, id, password):
    data = load_data()

    #사용자 정보 확인
    for user in data["users"]:
        if user["username"] == username:
            return False, "이미 사용 중인 사용자 이름입니다."
        if user["id"] == id:
            return False, "이미 사용 중인 아이디입니다."
        if user["password"] == password:
            return False, "이미 사용 중인 비밀번호입니다."
    
     # 사용자 정보 저장
    new_user = {
        "username": username,
        "id": id,
        "password": password  # 비밀번호 저장 전에 해싱 또는 암호화 필요
    }
    data["users"].append(new_user)
    save_data(data)
    
    return True, "회원가입이 완료되었습니다."
    


def create_post(username, title, content):
    data = load_data()
    new_post = {
        "num": len(data["posts"]) + 1,
        "username":username,
        "title": title,
        "content": content,
        "date_posted": datetime.utcnow().isoformat(),
        "comments": []
    }
    data["posts"].append(new_post)
    save_data(data)
    return new_post

def add_comment(username, post_id, content):
    data = load_data()
    comment = {
        "num": len(data["comments"]) + 1,
        "username": username,
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