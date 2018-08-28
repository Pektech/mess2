from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_ask import Ask
from flask_marshmallow import Marshmallow
from afg import Supervisor

db = SQLAlchemy()
migrate = Migrate()
#ask = Ask(app, '/')

ma = Marshmallow()