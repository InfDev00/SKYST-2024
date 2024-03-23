from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash

from app import app, USERS_DATA
from app.data import load_data, save_data, authenticate, get_user

@app.route('/mypage')
def mypage():
    if 'user_id' not in session:
        flash('로그인이 필요합니다.', 'error')
        return redirect(url_for('login'))
    
    user = get_user(session['user_id'])
    if not user:
        flash('사용자 정보를 찾을 수 없습니다.', 'error')
        return redirect(url_for('login'))

    return render_template('mypage.html', user=user)