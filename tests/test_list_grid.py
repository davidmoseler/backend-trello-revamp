import unittest
from models import List, ListGrid
from app import app, db

class TestList(unittest.TestCase):
    def test_list_relationship(self):
        with app.app_context():
            list_grid = ListGrid()
            list1 = List(title='First list', position=1, list_grid=list_grid)
            list2 = List(title='Second list', position=2, list_grid=list_grid)
            db.session.add_all([list_grid, list1, list2])
            db.session.commit()
            self.assertEqual(list(list_grid.lists), [list1, list2])

if __name__ == '__main__':
    unittest.main()
