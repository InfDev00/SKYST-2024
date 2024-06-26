import json
from datetime import datetime

from app import POSTS_DATA, USERS_DATA, BANDS_DATA


# default function
def load_data(key):
    try:
        with open(key, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        if key == POSTS_DATA:
            data = {"posts": [], "comments": []}
        elif key == USERS_DATA or key == BANDS_DATA:
            data = []
    return data


def save_data(data, key):
    with open(key, 'w') as file:
        json.dump(data, file, indent=4)


# gallery function
def create_post(title, user_id, content):
    data = load_data(POSTS_DATA)
    new_post = {
        "post_id": len(data["posts"]) + 1,
        "username": get_user(user_id)['username'],
        "user_id": user_id,
        "title": title,
        "content": content,
        "date_posted": datetime.utcnow().isoformat(),
    }
    data["posts"].append(new_post)
    save_data(data, POSTS_DATA)
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
    save_data(data, POSTS_DATA)
    return comment


def get_posts(user_id):
    data = load_data(POSTS_DATA)

    user_posts = []
    for value in data["posts"]:
        if value["user_id"] == user_id:
            user_posts.append(value)

    return user_posts


def get_post(post_id):
    data = load_data(POSTS_DATA)
    for post in data["posts"]:
        if post["post_id"] == post_id:
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
def authenticate(id, password):
    users = load_data(USERS_DATA)
    if id in users and password == users[id]["password"]:
        return True
    return False


def register_user(username, id, password):
    data = load_data(USERS_DATA)
    # 사용자 정보 확인
    for key in data.keys():
        if data[key]["id"] == id:
            return False, "이미 사용 중인 아이디입니다."

    # 사용자 정보 저장
    new_user = {
        "username": username,
        "id": id,
        "password": password,  # 비밀번호 저장 전에 해싱 또는 암호화 필요        
        "bands": [],
        "lover": None
    }
    data[id] = new_user
    save_data(data, USERS_DATA)

    return True, "회원가입이 완료되었습니다."


def get_user(id):
    users = load_data(USERS_DATA)
    return users.get(id)


def add_lover(id, lover_id):
    user = get_user(id)
    lover = get_user(lover_id)

    if not user or not lover:
        return False  # error

    if not user['lover'] and not lover['lover']:
        user['lover'] = lover
        lover['lover'] = user
        return True
    return False


# def add_friend(id, friend_id):
#     user = get_user(id)
#     friend = get_user(friend_id)

#     if not user or not friend:
#         return False  # error

#     user['friends'].append(friend)
#     return True


#band function
def create_band(bandname, user_id, comment):
    data = load_data(BANDS_DATA)
    user = get_user(user_id)
    lover = user['lover']

    new_band = {
        "band_id": len(data)+1,
        "bandname": bandname,
        "comment": comment,
        "member": [user['id'], lover['id']]
    }
    user['bands'].append(new_band)
    lover['bands'].append(new_band)
    data.append(new_band)
    return new_band

def get_bands():
    data = load_data(BANDS_DATA)
    return data

def get_band(band_id):
    data = load_data(BANDS_DATA)
    for band in data:
        if band['band_id']==band_id:
            return band
    return None

def enter_band(band_id, user_id):
    band = get_band(band_id)
    user = get_user(user_id)
    lover = user['lover']
    
    band["member"].append(user)
    band["member"].append(lover)

    user['bands'].append(band)
    lover['bands'].append(band)

    return band

def get_band_id(band_id):
    band = get_band(band_id)
    return band["member"]