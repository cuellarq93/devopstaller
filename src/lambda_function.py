import json

def lambda_handler(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello, this is a mock response",
            "data": [1, 2, 3, 4]
        })
    }
    return response
