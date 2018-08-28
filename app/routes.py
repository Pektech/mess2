from mess2 import app
import os




@app.route('/')
def hello_world():
    show_env = os.environ.get('FLASK_ENV')
    print(show_env)
    return 'Hello Pek and Monk'