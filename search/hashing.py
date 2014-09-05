# -*- coding: utf-8 -*-
import hashlib
import uuid


def hash_password(password, salt):
    m = hashlib.sha512()
    m.update(password)
    m.update(salt)
    return unicode(m.hexdigest())


def get_salt():
    return str(uuid.uuid4().get_hex())