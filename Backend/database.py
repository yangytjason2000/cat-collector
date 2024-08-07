from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
db = SQLAlchemy()

connection_string = os.getenv('DB_CONNECTION_STRING')

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
    db.init_app(app)