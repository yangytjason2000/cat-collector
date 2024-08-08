from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
db = SQLAlchemy()

db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_port = os.getenv('DB_PORT')
connection_string = f"postgresql://{db_username}:{db_password}@localhost:{db_port}/cat_collector"

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
    db.init_app(app)