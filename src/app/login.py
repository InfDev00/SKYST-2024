from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash

from app import app, USERS_DATA
from app.data import load_data, save_data, authenticate, register_user, get_user


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        id = request.form['id']

        is_regist, text = register_user(username, id, password)

        if is_regist:
            flash(text, 'success')
            return redirect(url_for('login'))
        
        flash(text, 'error')
        return redirect(url_for('signup'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form['ids']
        password = request.form['password']
        if authenticate(id, password):
            session['username'] = get_user(id)['username']
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