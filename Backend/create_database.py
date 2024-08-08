import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import requests
from app import app
from models import db, Cat

load_dotenv()

THE_CAT_API_URL = os.getenv('THE_CAT_API_URL')
THE_CAT_API_KEY = os.getenv('THE_CAT_API_KEY')

def create_database_and_schema(db_name, user, password, host='localhost', port='5432'):
    # Create the database using credentials provided in .env file
    try:
        # Connect to the default database
        conn = psycopg2.connect(dbname='postgres', user=user, password=password, host=host, port=port)
        conn.autocommit = True
        cursor = conn.cursor()

        # Create the database
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
        print(f"Database '{db_name}' created successfully.")

        cursor.close()
        conn.close()

        # Connect to the newly created database and execute the schema
        conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()
        
        with open('./db_scripts/schema.sql', 'r') as file:
            schema = file.read()

        cursor.execute(schema)
        
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Schema for '{db_name}' applied successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

def fetch_random_cats():
    try:
        response = requests.get(THE_CAT_API_URL, headers={'x-api-key': THE_CAT_API_KEY}, params={'limit': 100})
        cats_data = response.json()

        for cat_data in cats_data:
            cat = Cat(api_id=cat_data['id'], image_url=cat_data['url'])
            db.session.add(cat)

        db.session.commit()
        print("Random cats have been fetched and stored successfully.")
    except Exception as e:
        print(f"An error occurred while fetching cats: {e}")

if __name__ == '__main__':
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    db_port = os.getenv('DB_PORT')

    create_database_and_schema('cat_collector', db_username, db_password, port=db_port)

    with app.app_context():
        fetch_random_cats()