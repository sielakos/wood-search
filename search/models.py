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

    def to_dict(self):
        product_dict = {
            '_id': str(self['_id']),
            'name': self.name,
            'price': self.price,
            'description': self.description
        }

        if self.company is not None:
            product_dict['company'] = {
                '_id': str(self.company['_id']),
                'name': self.company.name
            }

        return product_dict

    @property
    def company(self):
        #TODO: implement good cache mechanism
        if self.company_id is not None:
            return db.Company.get_from_id(self.company_id)
        return None


@db.register
class Company(Document):
    __collection__ = 'companies'
    structure = {
        'name': unicode,
        'description': unicode,
        'products_ids': []
    }

    required_fields = ['name', 'description']

    use_dot_notation = True