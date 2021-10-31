from flask import Flask

# app config file
from config import Config

# create the application instance
app = Flask(__name__)
app.config.from_object(Config)

# create the application database instance
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

from app import routes
