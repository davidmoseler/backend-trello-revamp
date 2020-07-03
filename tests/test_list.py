import unittest
from models import List, Card
from app import app, db

class TestList(unittest.TestCase):
    def test_card_relationship(self):
        with app.app_context():
            list_ = List(title='First list')
            card1 = Card(text='First card', position=1, list=list_)
            card2 = Card(text='Second card', position=2, list=list_)
            db.session.add_all([card1, card2, list_])
            db.session.commit()
            self.assertEqual(list(list_.cards), [card1, card2])

if __name__ == '__main__':
    unittest.main()
