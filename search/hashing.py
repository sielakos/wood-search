# -*- coding: utf-8 -*-
import hashlib
import uuid


def hash_password(password, salt):
    m = hashlib.sha512()
    m.upadte(password)
    m.update(salt)
    return str(m.hexdigest())


def get_salt():
    return str(uuid.uuid4().get_hex())