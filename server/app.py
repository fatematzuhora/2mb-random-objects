"""
main module of the server file
"""
from config import Config
from app import app

if __name__ == '__main__':
    app.secret_key=Config.SECRET_KEY
    app.run(host='0.0.0.0', port=8080, debug=True)
