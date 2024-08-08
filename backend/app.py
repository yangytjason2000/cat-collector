from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS
from models import Cat, FavoriteCat
from database import db, init_db
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)
api = Api(app)
init_db(app)

class CatList(Resource):
    #Return a list of all cats in the database based on page number and limit, used for pagination
    def get(self):
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 10, type=int)

        pagination = Cat.query.order_by(Cat.id).paginate(page=page, per_page=limit, error_out=False)
    
        cats = pagination.items

        return jsonify([{'id': cat.id, 'api_id': cat.api_id, 'image_url': cat.image_url,
                         'name': cat.name, 'description': cat.description, 'is_favorite': cat.favorite is not None} for cat in cats])

    #Add a new cat to the favorite table, indicating the cat being added to favorite_cat
    def post(self):
        data = request.json
        new_favorite = FavoriteCat(cat_id=data['cat_id'])
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({'message': 'Cat added to favorites', 'cat': new_favorite.cat_id})

class CatDetail(Resource):
    #Return the detail information of a cat by a given id
    def get(self, cat_id):
        cat = db.session.get(Cat,cat_id)
        return jsonify({'id': cat.id, 'api_id': cat.api_id, 'image_url': cat.image_url,
                        'name': cat.name, 'description': cat.description, 'is_favorite': cat.favorite is not None})

    #Update name or description of a cat by a given id
    def put(self, cat_id):
        cat = db.session.get(Cat,cat_id)
        data = request.json
        cat.name = data.get('name', cat.name)
        cat.description = data.get('description', cat.description)
        db.session.commit()
        return jsonify({'message': 'Cat updated', 'cat': cat_id})

    #Remove the cat from favorite_cat table, indicating the cat being removed from favorite
    def delete(self, cat_id):
        favorite_cat = db.session.get(FavoriteCat,cat_id)
        db.session.delete(favorite_cat)
        db.session.commit()
        return jsonify({'message': 'Cat removed from favorites', 'cat': cat_id})

api.add_resource(CatList, '/cats')
api.add_resource(CatDetail, '/cats/<int:cat_id>')

if __name__ == '__main__':
    app.run(debug=True)