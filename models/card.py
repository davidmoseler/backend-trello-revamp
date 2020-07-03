from .db import db

class Card(db.Model):
    __tablename__ = 'card'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    position = db.Column(db.Integer)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'))
