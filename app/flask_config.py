import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    DEBUG=False
    SECRET_KEY = os.environ.get('MESS_SECRET')
    SQLALCHEMY_DATABASE_URI = os.environ.get('MESS2_DB') or \
        'sqlite:///' + os.path.join(basedir, 'mess2.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(BaseConfig):
    DEBUG=False

class DevConfig(BaseConfig):
    DEBUG=True

class TestConfig(BaseConfig):
    DEBUG=True
    #SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DB') or \
    #  'sqlite:///' + os.path.join(basedir, 'test_mess.db')

