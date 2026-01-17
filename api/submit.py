import json

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": json.dumps({"message": "Method not allowed"})
        }

    body = json.loads(request.body)

    zip_code = body.get("zip")
    food = body.get("food")

    print("Received:", zip_code, food)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Data received successfully"
        })
    }
