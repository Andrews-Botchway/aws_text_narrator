import boto3
import json
import time

polly = boto3.client('polly')
s3 = boto3.client('s3')

# S3 bucket where audio files will be stored
AUDIO_BUCKET_NAME = "aws-polly-audio-files-storage-gemini"  # Replace with your audio bucket name

# S3 bucket where text files are stored
TEXT_BUCKET_NAME = "aws-text-files-storage-gemini"  # Replace with your text S3 bucket name here

def lambda_handler(event, context):
    try:
        # Get S3 text bucket and file name from event
        text_bucket = event.get('text_bucket', TEXT_BUCKET_NAME)
        text_key = event.get('text_key')
        if not text_key:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "No text file key provided"})
            }

        # Fetch text from S3
        text_obj = s3.get_object(Bucket=text_bucket, Key=text_key)
        text = text_obj['Body'].read().decode('utf-8').strip()

        if not text:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Text file is empty"})
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
            Bucket=AUDIO_BUCKET_NAME,
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

if __name__ == "__main__":
    # Allow running from terminal
    text_key = input("Enter the name of the text file in the text S3 bucket: ").strip()
    event = {
        "text_bucket": TEXT_BUCKET_NAME,
        "text_key": text_key
    }
    # context is not used, so pass None
    result = lambda_handler(event, None)
    print(result)