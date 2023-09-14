# import requests

def lambda_handler(event, context):
    print(event)
    print("Hello FunctionThree")

    return {
        "statusCode": 200,
        "body": {
            "message": "Hello FunctionThree",
            # "location": ip.text.replace("\n", "")
        },
    }