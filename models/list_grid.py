from .db import db

class ListGrid(db.Model):
    __tablename__ = 'list_grid'

    id = db.Column(db.Integer, primary_key=True)
    lists = db.relationship('List', backref='list_grid', lazy='dynamic')
