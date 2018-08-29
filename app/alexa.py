from app import db, ma
from mess2 import app
from .models import User, Family, Messages
from flask_ask import question, Ask
from flask_ask import session as ask_session
from flask import render_template, Blueprint
from afg import Supervisor
from sqlalchemy.exc import SQLAlchemyError
import logging
from .models import MessagesSchema

logging.getLogger('flask_ask').setLevel(logging.DEBUG)
blueprint = Blueprint('intents', __name__,template_folder='templates' , url_prefix='/ask')
ask=Ask(blueprint=blueprint)
sup = Supervisor('scenario.yaml')

@ask.on_session_started
@sup.start
def new_session():
    app.logger.debug('new user session started')


@sup.stop
def close_user_session():
    app.logger.debug("user session stopped")


@ask.session_ended
def session_ended():
    close_user_session()
    return '', 200


@ask.intent('AMAZON.HelpIntent')
@sup.guide
def help_user():
    context_help = sup.get_help()
    return question(context_help)


@ask.launch
@sup.guide
def launched():
    ask_session.attributes['stage'] = 'start'
    ask_session.attributes['alexa_id'] = '999'  # hardcoded just for testing
    return question(render_template('welcome'))


@ask.intent('SayName')
@sup.guide
def my_name(name):
    if name is None:
        return sup.reprompt_error("I really need your name")