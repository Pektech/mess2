import os
from app import  create_app, db, ma
from app.models import User, Messages, Family
from app.flask_config import ProdConfig, DevConfig




app =  create_app()


from app import routes, models, alexa

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Family': Family, 'Messages': Messages,
            'ma': ma}
