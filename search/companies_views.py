# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, request
from app import app
from database import db
from filters import replace_nl


@app.route('/show_companies')
def show_companies():
    companies = db.Company.find()
    return render_template('show_companies.html', companies=companies)


@app.route('/add_company', methods=['GET', 'POST'])
def add_company():
    if request.method == 'POST':
        company = db.Company()
        company.name = replace_nl(request.form['name'], put_in='')
        company.description = replace_nl(request.form['description'])
        company.validate()
        company.save()
        return redirect(url_for('show_companies'))

    return render_template('add_company.html')
