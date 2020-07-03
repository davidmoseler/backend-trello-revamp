from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import ListGrid, List, Card
from models.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://trello:trello@localhost:5432/trello_revamp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/list_grid/<id>', methods=['GET'])
def show_list_grid(id):
    list_grid = ListGrid.query.filter_by(id=id).one()
    json = []
    for list_ in list_grid.lists.order_by(List.position):
        json.append({
                'id': list_.id,
                'position': list_.position,
                'title': list_.title,
                'cards': [{'text': card.text} for card in list_.cards.order_by(Card.position)]
                })
    return jsonify(json)

@app.route('/list_grid', methods=['POST'])
def create_list_grid():
    json = request.json
    list_grid = ListGrid()
    db.session.add(list_grid)
    for i, list_ in enumerate(json):
        cards = list_['cards']
        list_ = List(
                list_grid = list_grid,
                position = i,
                title = list_['title']
                )
        db.session.add(list_)
        for i, card in enumerate(cards):
            card = Card(
                    text = card['text'],
                    list = list_,
                    position = i
                    )
            db.session.add(card)
    db.session.commit()
    return {'list_grid': list_grid.id}

@app.route('/list_grid', methods=['POST'])
def create_list_grid():
    json = request.json
    list_grid = ListGrid()
    db.session.add(list_grid)
    for i, list_ in enumerate(json):
        cards = list_['cards']
        list_ = List(
                list_grid = list_grid,
                position = i,
                title = list_['title']
                )
        db.session.add(list_)
        for i, card in enumerate(cards):
            card = Card(
                    text = card['text'],
                    list = list_,
                    position = i
                    )
            db.session.add(card)
    db.session.commit()
    return {'list_grid': list_grid.id}

@app.route('/list_grid/<id>', methods=['PUT'])
def update_list_grid(id):
    json = request.json
    list_grid = ListGrid.query.filter_by(id=id).one()
    list_ids = [list_.id for list_ in list_grid]
    for i, list_ in enumerate(json):
        cards = list_['cards']
        list_ = List(
                list_grid = list_grid,
                position = i,
                title = list_['title']
                )
        db.session.add(list_)
        card_ids = [card.id for card in list_.cards]
        for i, card in enumerate(cards):
            card = Card(
                    text = card['text'],
                    list = list_,
                    position = i
                    )
            db.session.add(card)
        for id in card_ids:
            if id not in [card['id'] for card in cards]:
                db.session.delete(Card.query.filter_by(id=id).one())
    for id in list_ids:
        if id not in [list_['id'] for list_ in list_grid]:
            db.session.delete(List.query.filter_by(id=id).one())
    db.session.commit()
    return {'list_grid': list_grid.id}
