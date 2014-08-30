# -*- coding: utf-8 -*-
from flask.ext.mongokit import MongoKit
from search.app import app

db = MongoKit(app)