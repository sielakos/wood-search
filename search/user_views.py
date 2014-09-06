# -*- coding: utf-8 -*-
from app import app
from auth import has_role_decorator, logged_in_decorator, get_current_user, redirect_on_false_decorator, has_role
from flask import render_template
from database import db


@app.route('/user/profile')
@logged_in_decorator
def user_profile():
    user = get_current_user()
    return render_template('user/profile.html', user=user)


@app.route('/user/change_password/<ObjectId:user_id>', methods=['GET', 'POST'])
def user_change_password(user_id):
    user = db.User.find_one_or_404({'_id': user_id})
    current_user = get_current_user()

    @redirect_on_false_decorator(user == current_user or has_role('ROLE_ADMIN', user=user))
    def action():
        return render_template('user/change_password.html', user=user)

    return action()