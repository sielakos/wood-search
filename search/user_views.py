# -*- coding: utf-8 -*-
from app import app
from auth import has_role_decorator, logged_in_decorator, get_current_user, redirect_on_false_decorator, has_role, request
from flask import render_template, redirect, url_for, flash
from database import db
from hashing import hash_password


@app.route('/user/profile')
@logged_in_decorator
def user_profile():
    user = get_current_user()
    return render_template('user/profile.html', user=user)


def verify_password_change(user):
    old_password = request.form['old-password']
    pass_hash = hash_password(old_password, user.salt)
    return (pass_hash == user.pass_hash or has_role('ROLE_ADMIN')) and \
        request.form['new-password'] == request.form['repeat-new-password']


def change_password_for_user(user):
    pass


@app.route('/user/change_password/<ObjectId:user_id>', methods=['GET', 'POST'])
def user_change_password(user_id):
    user = db.User.find_one_or_404({'_id': user_id})
    current_user = get_current_user()

    @redirect_on_false_decorator(user == current_user or has_role('ROLE_ADMIN', user=current_user))
    def action():
        error = None
        if request.method == 'POST':
            if verify_password_change(user):
                change_password_for_user(user)
                flash('Your password was changed!')
                return redirect(url_for('index'))
            else:
                error = 'Incorrect form data'

        return render_template('user/change_password.html', user=user, error=error)

    return action()