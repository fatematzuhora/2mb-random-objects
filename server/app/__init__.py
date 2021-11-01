"""
init file
"""
from flask import Flask

# app config file
from config import Config

# create the application instance
app = Flask(__name__)
app.config.from_object(Config)

from app import routes
