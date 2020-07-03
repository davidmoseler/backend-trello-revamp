from .ApiTest import ApiTest

class ListGridApiTest(ApiTest):
    def test_creates_list_grid(self):
        json = [
                {'title': 'First list',
                 'cards': [
                     {'text': 'First card'},
                     {'text': 'Second card'}
                 ]
                },
                {'title': 'Second list',
                 'cards': [
                     {'text': 'Third card'},
                     {'text': 'Fourth card'},
                     {'text': 'Fifth card'}
                 ]
                }
            ]
        res = self.app.post('/list_grid', headers={"Content-Type": "application/json"}, json=json)
        id = res.get_json()['list_grid']

        res = self.app.get('/list_grid/{}'.format(id))
        res = [
                {'title': list_['title'], 'cards': list_['cards']} for list_ in res.get_json()
                ]
        self.assertEqual(res, json)
