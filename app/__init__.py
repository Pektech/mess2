import os

from flask import Flask

from .extensions import db, migrate, ma
from flask_ask import Ask

from afg import Supervisor
from flask_marshmallow import Marshmallow
config = {
    "development": "app.flask_config.DevConfig",
    "testing": "app.flask_config.TestConfig",
    "default": "app.flask_config.DevConfig",
    'prof' : 'app.flask_config.ProdConfig'

}
def create_app():
    config_name = os.getenv('FLASK_ENV', 'default')
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    print(config[config_name])

    register_extensions(app)



    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    #ask = Ask(app, '/')
    #sup = Supervisor('app/scenario.yaml')

    ma.init_app(app)


