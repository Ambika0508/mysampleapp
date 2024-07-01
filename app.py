from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import boto3
from botocore.exceptions import ClientError
import os
import subprocess
import json

app = FastAPI()

# Initialize a session using Amazon S3
s3 = boto3.client('s3', verify=False)

@app.get("/")
async def home():
    return {"message": "Welcome to the Python Sample Application "}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000, log_level="debug")
