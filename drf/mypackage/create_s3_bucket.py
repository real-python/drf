import logging
import boto3
from botocore.exceptions import ClientError
import uuid


ud = 'kuntal12345'
aws_access_key_id = ''
aws_secret_access_key = ''

try:
    client = boto3.client(
        's3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    client.create_bucket(Bucket=ud)
except Exception as e:
    print(e)
else:
    print("Bucket Name : ", ud)
