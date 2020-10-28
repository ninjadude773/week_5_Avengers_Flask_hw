from flask import Flask

#Import the Config Object
from config import Config

# Import for the SQLAlchemy Object
from flask_sqlalchemy import SQLAlchemy

# Import the Migrate Object
from flask_migrate import Migrate

app = Flask(__name__)
# Complete the Config cycle for our Flask App
# And give access to our database (when we have one)
# along with out secret key
app.config.from_object(Config)

# Init our Database (db)
db = SQLAlchemy(app)

# Init the Migrator
migrate = Migrate(app,db)

from avengers_form_app import routes,models