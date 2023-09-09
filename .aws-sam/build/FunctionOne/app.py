# import requests

def lambda_handler(event, context):
    print(event)
    print("Hello01")

    return {
        "statusCode": 200,
        "body": {
            "message": "Hello FunctionOne",
            # "location": ip.text.replace("\n", "")
        },
    }