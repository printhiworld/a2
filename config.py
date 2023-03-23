import hashlib


class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def get_hash(self):
    print( hashlib.md5(self.password.encode('utf-8')).hexdigest())

