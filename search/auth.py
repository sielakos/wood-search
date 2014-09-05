# -*- coding: utf-8 -*-
from search.app import app
from search.database import db
from flask import session, redirect, url_for, render_template, request
from functools import wraps
from search.hashing import get_salt, hash_password


