"""
main module of the server file
"""
from config import Config
from app import app

# @app.before_first_request
# def create_tables():

if __name__ == '__main__':
    app.secret_key=Config.SECRET_KEY
    app.run(host='0.0.0.0', port=8080, debug=True)
