# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, request
from app import app
from database import db
from filters import replace_nl
from auth import has_role_decorator, is_owner_decorator


@app.route('/companies/')
def show_companies():
    companies = db.Company.find()
    return render_template('company/show_companies.html', companies=companies)


@app.route('/companies/add', methods=['GET', 'POST'])
@has_role_decorator('ROLE_ADMIN')
def add_company():
    if request.method == 'POST':
        company = db.Company()
        company.name = replace_nl(request.form['name'], put_in='')
        company.description = replace_nl(request.form['description'])
        company.validate()
        company.save()
        return redirect(url_for('show_companies'))

    return render_template('company/add_company.html')


@app.route('/companies/edit/<ObjectId:company_id>', methods=['GET', 'POST'])
def edit_company(company_id):
    company = db.Company.get_from_id(company_id)

    @is_owner_decorator(company['_id'])
    def action():
        if request.method == 'POST':
            company.name = request.form['name']
            company.description = replace_nl(request.form['description'])
            company.save()
            return redirect(url_for('show_company'))

        return render_template('company/edit_company.html', company=company)

    return action()


@app.route('/companies/show/<ObjectId:company_id>')
def show_company(company_id):
    company = db.Company.get_from_id(company_id)
    return render_template('company/show_company.html', company=company)


@app.route('/companies/remove/<ObjectId:company_id>', methods=['GET', 'POST'])
def remove_company(company_id):
    company = db.Company.get_from_id(company_id)

    @is_owner_decorator(company['_id'])
    def action():
        company.remove_products()
        company.delete()
        return redirect(url_for('show_companies'))

    return action()