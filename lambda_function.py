import boto3
import json
import time

polly = boto3.client('polly')
s3 = boto3.client('s3')

BUCKET_NAME = "aws-polly-audio-files-storage-gemini"  # Replace with your bucket name

def lambda_handler(event, context):
    try:
        text = event.get('text')
        if not text:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "No text provided"})
            }

        # Synthesize speech using Polly
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId="Joanna"
        )

        # Generate a unique key for the audio file
        key = f"audio-{int(time.time() * 1000)}.mp3"

        # Upload the audio stream to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=key,
            Body=response['AudioStream'].read(),
            ContentType="audio/mpeg"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": f"Audio file stored as {key}"})
        }
    except Exception as error:
        print("Error:", error)
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"})
        }
