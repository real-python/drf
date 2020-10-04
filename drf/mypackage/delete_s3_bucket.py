import logging
import boto3
from botocore.exceptions import ClientError
import os
import shutil


bucket_name = input("Enter : ")
aws_access_key_id = ''
aws_secret_access_key = ''

try:
    client = boto3.client(
        's3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    client.delete_bucket(
        bucket=bucket_name
    )
except Exception as e:
    print("\n\n", e, "\n\n")
    bucket = boto3.resource(
        's3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key
    ).Bucket(bucket_name)
    bucket.objects.all().delete()
    bucket.delete()