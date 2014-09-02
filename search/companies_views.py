# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, request
from app import app
from database import db
from filters import replace_nl


@app.route('/companies/')
def show_companies():
    companies = db.Company.find()
    return render_template('show_companies.html', companies=companies)


@app.route('/companies/add', methods=['GET', 'POST'])
def add_company():
    if request.method == 'POST':
        company = db.Company()
        company.name = replace_nl(request.form['name'], put_in='')
        company.description = replace_nl(request.form['description'])
        company.validate()
        company.save()
        return redirect(url_for('show_companies'))

    return render_template('add_company.html')


@app.route('/companies/edit/<ObjectId:company_id>', methods=['GET', 'POST'])
def edit_company(company_id):
    company = db.Company.get_from_id(company_id)

    if request.method == 'POST':
        company.name = request.form['name']
        company.description = replace_nl(request.form['description'])
        company.save()
        return redirect(url_for('show_companies'))

    return render_template('edit_company.html', company=company)


@app.route('/companies/show/<ObjectId:company_id>')
def show_company(company_id):
    company = db.Company.get_from_id(company_id)
    return render_template('show_company.html', company=company)