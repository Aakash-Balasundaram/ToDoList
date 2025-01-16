import boto3
import base64

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Extract file details from event
    file_name = event.get("file_name", "default.pdf")
    file_content = event.get("file_content")  # Base64 encoded content
    bucket_name = event.get("bucket_name", "my-default-bucket")
    
    try:
        # Decode the file content
        file_bytes = base64.b64decode(file_content)

        # Upload the file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_bytes)

        return {
            "statusCode": 200,
            "body": {
                "message": f"File {file_name} uploaded successfully to {bucket_name}."
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": {
                "message": "File upload failed.",
                "error": str(e)
            }
        }
