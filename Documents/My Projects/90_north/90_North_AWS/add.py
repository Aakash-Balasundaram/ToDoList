def lambda_handler(event, context):
    # Extract numbers from the input
    num1 = event.get("num1", 0)
    num2 = event.get("num2", 0)
    
    # Calculate the result
    result = num1 + num2

    return {
        "statusCode": 200,
        "body": {
            "message": "Addition Successful",
            "result": result
        }
    }
