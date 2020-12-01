# Dash app initialization
import dash
import dash_bootstrap_components as dbc

# global imports
from flask_login import LoginManager, UserMixin

# local imports
from utilities.auth import db, User as base
from utilities.config import config, engine

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.15.1/css/all.css"
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, FONT_AWESOME]
)

server = app.server
app.config.suppress_callback_exceptions = True
# app.css.config.serve_locally = True
# app.scripts.config.serve_locally = True
app.title = 'Bioinformatics'

# config
server.config.update(
    SECRET_KEY='make this key random or hard to guess',
    SQLALCHEMY_DATABASE_URI=config.get('database', 'con'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db.init_app(server)

# Setup the LoginManager for the server
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'

curr_user = None  # variable to save a User object instance of the current logged in user


# Create User class with UserMixin
class User(UserMixin, base):
    def __init__(self, user):
        self.id = user['user']
        self.user = user['user']
        self.first = user['first']
        self.last = user['last']
        self.email = user['email']
        self.level = user['level']
        # self.password = user['password']

        self.is_active = True
        self.is_authenticated = True
        self.is_anonymous = False  # anonymous users are not allowed

        global curr_user
        curr_user = self

    def is_active(self):
        return self.is_active

    def is_authenticated(self):
        return self.is_authenticated

    def is_anonymous(self):
        return self.is_anonymous

    def get_id(self):
        return self.id


# callback to reload the user object
@login_manager.user_loader
def load_user(user_id):
    print('>>> load_user():', str(user_id))
    return curr_user
