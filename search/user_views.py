# -*- coding: utf-8 -*-
from app import app
from auth import has_role_decorator, logged_in_decorator, get_current_user
from flask import render_template


@app.route('/user/profile')
@logged_in_decorator
def user_profile():
    user = get_current_user()
    return render_template('user/profile.html', user=user)