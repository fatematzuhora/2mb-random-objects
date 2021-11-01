"""
init file
"""
from flask import Flask
from flask_cors import CORS

# app config file
from config import Config

# create the application instance
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object(Config)

from app import routes
