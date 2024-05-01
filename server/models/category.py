from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from config import flask_bcrypt, db
from sqlalchemy import event

class Category(db.Model, SerializerMixin):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    parent = db.relationship('Category', remote_side=[id], backref='children')


    patterns = db.relationship('Pattern', back_populates='category')


    @classmethod
    def create_category(cls, name, description, parent_id=None):
        category = cls(name=name, description=description, parent_id=parent_id)
        db.session.add(category)
        db.session.commit()
        return category

@event.listens_for(Category.__table__, 'after_create')
def create_initial_categories(*args, **kwargs):
    knit = Category(name='Knit', description='Knitting related patterns')
    crochet = Category(name='Crochet', description='Crocheting related patterns')
    db.session.add_all([knit, crochet])
    db.session.commit()