import unittest
import json
from src.lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    def test_lambda_handler(self):
        event = {}
        context = {}
        response = lambda_handler(event, context)
        
        self.assertEqual(response['statusCode'], 200)
        
        body = json.loads(response['body'])
        self.assertEqual(body['message'], "Hello, this is a mock response")
        self.assertEqual(body['data'], [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
