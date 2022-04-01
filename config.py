from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init flask app
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Something'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from models import User

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))