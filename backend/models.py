from database import db

class Cat(db.Model):
    __tablename__ = 'cats'
    
    id = db.Column(db.Integer, primary_key=True)
    api_id = db.Column(db.String(100), unique=True, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))

    favorite = db.relationship('FavoriteCat', back_populates='cat', uselist=False)

class FavoriteCat(db.Model):
    __tablename__ = 'favorite_cats'
    
    cat_id = db.Column(db.Integer, db.ForeignKey('cats.id', ondelete='CASCADE'), primary_key=True, unique=True) 

    cat = db.relationship('Cat', back_populates='favorite')