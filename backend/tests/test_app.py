import pytest
from app import create_app
from database import db
from models import Cat, FavoriteCat

@pytest.fixture
def client():
    # Configure the Flask app for testing
    test_config = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    }
    
    app = create_app(test_config)

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

#Test for the GET /cats endpoint
def test_get_cats(client):
    response = client.get('/cats')
    
    assert response.status_code == 200
    
    assert response.json == []

#Test for the GET /cats/{id} endpoint
def test_get_cat_detail(client):
    with client.application.app_context():
        new_cat = Cat(api_id='1', image_url='http://example.com/cat.jpg', name='cat1', description='A nice cat', breed='Siamese')
        db.session.add(new_cat)
        db.session.commit()

        cat_id = new_cat.id

    response = client.get(f'/cats/{cat_id}')

    assert response.status_code == 200

    assert response.json == {
        'id': cat_id,
        'api_id': '1',
        'image_url': 'http://example.com/cat.jpg',
        'name': 'cat1',
        'description': 'A nice cat',
        'breed': 'Siamese',
        'is_favorite': False
    }

#Test for the POST /cats endpoint of adding a cat to favorite
def test_post_cat_favorite(client):
    with client.application.app_context():
        new_cat = Cat(api_id='2', image_url='http://example.com/cat2.jpg', name='cat2', description='A cute cat', breed='Siamese')
        db.session.add(new_cat)
        db.session.commit()

        cat_id = new_cat.id

    response = client.post('/cats', json={'cat_id': cat_id})

    assert response.status_code == 200

    assert response.json == {'message': 'Cat added to favorites', 'cat': cat_id}

    with client.application.app_context():
        favorite_cat = db.session.get(FavoriteCat, cat_id)
        assert favorite_cat is not None

#Test for the PUT /cats/{id} endpoint of updating detail of a cat
def test_put_cat_detail(client):
    with client.application.app_context():
        new_cat = Cat(api_id='3', image_url='http://example.com/cat3.jpg', name='cat3', description='A curious cat', breed='Siamese')
        db.session.add(new_cat)
        db.session.commit()

        cat_id = new_cat.id

    response = client.put(f'/cats/{cat_id}', json={'name': 'Name updated', 'description': 'Description updated', 'breed': 'Breed updated'})

    assert response.status_code == 200

    assert response.json == {'message': 'Cat updated', 'cat': cat_id}

    with client.application.app_context():
        updated_cat = db.session.get(Cat, cat_id)
        assert updated_cat.name == 'Name updated'
        assert updated_cat.description == 'Description updated'
        assert updated_cat.breed == 'Breed updated'

#Test for the DELETE /cats/{id} endpoint of removing a cat from favorite
def test_delete_cat_favorite(client):
    with client.application.app_context():
        new_cat = Cat(api_id='4', image_url='http://example.com/cat4.jpg', name='cat4', description='A interesting cat', breed='')
        db.session.add(new_cat)
        db.session.commit()

        favorite_cat = FavoriteCat(cat_id=new_cat.id)
        db.session.add(favorite_cat)
        db.session.commit()

        cat_id = new_cat.id

    response = client.delete(f'/cats/{cat_id}')

    assert response.status_code == 200

    assert response.json == {'message': 'Cat removed from favorites', 'cat': cat_id}

    with client.application.app_context():
        removed_favorite_cat = db.session.get(FavoriteCat, cat_id)
        assert removed_favorite_cat is None