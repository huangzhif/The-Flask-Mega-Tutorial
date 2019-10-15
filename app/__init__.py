from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask(__name__,instance_relative_config=True)
app.config.from_object(Config)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
migrate = Migrate(app,db)

bootstrap = Bootstrap(app)

mail = Mail(app)

moment = Moment(app)

login = LoginManager(app)
login.login_view = "login"

from app import routes,models,errors

