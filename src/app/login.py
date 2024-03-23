from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash

from app import app, USERS_DATA
from app.data import load_data, save_data, authenticate


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username.strip() == '' or password.strip() == '':
            flash('사용자 이름과 비밀번호를 입력하세요.', 'error')
            return redirect(url_for('signup'))
        users = load_data(USERS_DATA)
        if username in users:
            flash('이미 존재하는 사용자입니다.', 'error')
            return redirect(url_for('signup'))
        users[username] = generate_password_hash(password)
        save_data(users, USERS_DATA)
        flash('회원가입이 완료되었습니다. 로그인하세요!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate(username, password):
            session['username'] = username
            flash('로그인 되었습니다.', 'success')
            return redirect(url_for('index'))
        else:
            flash('사용자 이름 또는 비밀번호가 올바르지 않습니다.', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('로그아웃 되었습니다.', 'info')
    return redirect(url_for('index'))