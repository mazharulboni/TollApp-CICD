# import requests

def lambda_handler(event, context):
    print(event)
    print("Hello FunctionTwo")

    return {
        "statusCode": 200,
        "body": {
            "message": "Hello FunctionTwo",
            # "location": ip.text.replace("\n", "")
        },
    }