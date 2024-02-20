def lambda_handler(event, context):
    # Print "Hello Ajay" to CloudWatch Logs
    print("Hello Ajay")
    # Return a response (optional)
    return {
        'statusCode': 200,
        'body': 'Hello Ajay'
    }
