# -*- coding: utf-8 -*-
from search.app import app
from search.database import db
from flask import session, redirect, url_for, render_template, request, flash
from search.hashing import get_salt, hash_password


def create_default_user():
    if db.User.find().count() == 0:
        user = db.User()
        user.name = unicode('admin')
        user.salt = get_salt()
        user.pass_hash = hash_password('password', user.salt)
        user.email = unicode('sielakos@gmail.com')
        user.roles = ['ROLE_ADMIN']
        user.save()


def check_login(user):
    if user is not None:
        pass_hash = hash_password(request.form['password'], user.salt)
        print("password: " + request.form['password'] + ", pass_hash: " + pass_hash + ", hash_from_db: " + user.pass_hash)
        return pass_hash == user.pass_hash
    else:
        return False


def correct_login_action(user):
    address = session.pop('login_redirect', url_for('index'))
    session['user'] = str(user['_id'])
    flash('You logged in as %s' % user.name)
    return redirect(address)


@app.route('/login', methods=['GET', 'POST'])
def login():
    create_default_user()

    if session.get('user', None) is not None:
        flash('You are already logged in')
        return redirect(url_for('index'))

    error = None
    if request.method == 'POST':
        name = request.form['name']
        user = db.User.fetch_one({'name': name})

        if check_login(user):
            return correct_login_action(user)
        else:
            error = 'Incorrect username or password'

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You were logged out')
    return redirect(url_for('index'))