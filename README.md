# Serverless Text-to-Speech Automation with Amazon Polly

## Overview
This project is a **serverless text-to-speech (TTS) application** built on AWS.  
Users can **upload text directly**, which is then processed by **AWS Lambda** and converted into **lifelike speech** using **Amazon Polly**.  
The generated audio files are stored in **Amazon S3**, making them easily accessible for playback or distribution.  

---

## Key Capabilities
- Converts **user-submitted text** into natural-sounding audio.
- Supports **voice, pitch, and speed customization** for narration.
- Fully **serverless and event-driven** architecture.
- Follows **IAM security best practices** for least-privilege access.
- Stores generated audio in **Amazon S3** for seamless retrieval.

---

## Technical Workflow
1. **User submits text** through the application.
2. **AWS Lambda (Python)** receives and processes the input.
3. **Amazon Polly** converts the text into an audio file (e.g., mp3).
4. The **audio file is stored in S3** and made available for playback or download.

---

## Process Steps
1. **Create an IAM Role** – Grant Lambda permissions for Polly and S3.  
2. **Create an S3 Bucket** – Store audio output files.  
3. **Deploy a Lambda Function (Python)** – Accepts input text and invokes Polly.  
4. **Test the Output** – Retrieve and validate audio files from S3.  

---

## AWS Services Used
- **Amazon Polly** – Neural text-to-speech engine.  
- **AWS Lambda (Python)** – Serverless compute for text processing.  
- **Amazon S3** – Storage for generated audio files.  
- **AWS IAM** – Secure access control via roles and policies.  

---

## Impact
This project demonstrates the ability to build **production-ready, serverless applications** that are:  
- **Scalable** – leveraging AWS managed services.  
- **Secure** – following IAM best practices.  
- **User-focused** – enabling accessible and automated content delivery.  

---

## Architecture Diagram
This is what the architecture looks like

![alt text](<Text-to-Speech architectural diagram.png>)

---

## Final Result
This is what your project result will look like, once built:

![alt text](<Final Result.png>)

