from .db import db

class List(db.Model):
    __tablename__ = 'list'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    cards = db.relationship('Card', backref='list', lazy='dynamic')
    position = db.Column(db.Integer)
    list_grid_id = db.Column(db.Integer, db.ForeignKey('list_grid.id'))

    def __repr__(self):
        return str(self.title)
