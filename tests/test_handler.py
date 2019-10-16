import unittest
import index
import json


class TestHandlerCase(unittest.TestCase):
      
    def test_e96(self):
        event = {
            'queryStringParameters': {
                'value': '249k'
            }
        }

        result = index.handler(
            event=event,
            context=None
        )

        response = json.loads(result['body'])

        self.assertEqual(response['closest']['E96']['nominal'], 249000)
        self.assertEqual(response['closest']['E96']['colors'][0], 'red')
        self.assertEqual(response['closest']['E96']['colors'][1], 'yellow')
        self.assertEqual(response['closest']['E96']['colors'][2], 'white')
        self.assertEqual(response['closest']['E96']['colors'][3], 'orange')
        self.assertEqual(response['closest']['E96']['colors'][4], 'brown')

    def test_e6(self):
        event = {
            'queryStringParameters': {
                'value': '6.8k'
            }
        }
    
        response = index.handler(
            event=event,
            context=None
        )
    
        response = json.loads(response['body'])
    
        self.assertEqual(response['closest']['E6']['nominal'], 6800)
        self.assertEqual(response['closest']['E6']['colors'][0], 'blue')
        self.assertEqual(response['closest']['E6']['colors'][1], 'grey')
        self.assertEqual(response['closest']['E6']['colors'][2], 'red')

    def test_e24(self):

        event = {
            'queryStringParameters': {
                'value': '750k'
            }
        }
    
        response = index.handler(
            event=event,
            context=None
        )
    
        response = json.loads(response['body'])
    
        self.assertEqual(response['closest']['E24']['nominal'], 750000)
        self.assertEqual(response['closest']['E24']['colors'][0], 'violet')
        self.assertEqual(response['closest']['E24']['colors'][1], 'green')
        self.assertEqual(response['closest']['E24']['colors'][2], 'yellow')
        self.assertEqual(response['closest']['E24']['colors'][3], 'gold')

    def test_path_e24(self):

        event = {
            'queryStringParameters': {'value': 1234},
            'pathParameters': {'series': 'e24'},
        }

        response = index.handler(event, None)

        response = json.loads(response['body'])

        self.assertEqual(response, 1200)

    def test_path_null(self):

        event = {
            'queryStringParameters': {'value': 1234},
            'pathParameters': None,
        }

        response = index.handler(event, None)

        self.assertEqual(response['statusCode'], 200)


if __name__ == '__main__':
    unittest.main()
