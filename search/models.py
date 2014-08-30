# -*- coding: utf-8 -*-
from database import db
from flask.ext.mongokit import Document
import datetime

@db.register
class Product(Document):
    __collection__ = 'products'
    structure = {
        'name': unicode,
        'description': unicode,
        'company_id': None,
        'created': datetime.datetime,
        'updated': datetime.datetime,
        'price': float
    }

    required_fields = ['name', 'description', 'company_id']

    default_values = {
        'created': datetime.datetime.utcnow,
        'updated': datetime.datetime.utcnow
    }

    use_dot_notation = True
    use_autorefs = True


@db.register
class Company(Document):
    __collection__ = 'companies'
    structure = {
        'name': unicode,
        'description': unicode,
        'products_ids': []
    }

    required_fields = ['name', 'description']

    use_autorefs = True