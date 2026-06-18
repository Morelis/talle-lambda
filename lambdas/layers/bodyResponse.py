import json

def bodyresponse(statusCode: int, body: dict) -> dict:
    return {
        'statusCode': statusCode,
        'body': json.dumps(body),
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        }
    }