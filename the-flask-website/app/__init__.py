from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# informational and debug log output with SQLAlchemy



# declare your variables here



app = Flask(__name__)
app.config.from_object(Config)
database = SQLAlchemy(app)
migrate = Migrate(app, database)




# flask login initializer 
login = LoginManager(app)
login.login_view ='login'

# connect_args = {'init_command':"SET @@collation_connection='utf8mb4_unicode_ci'"}





from app import routes
from app import models
