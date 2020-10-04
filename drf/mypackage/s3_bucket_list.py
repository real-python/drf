import logging
import boto3
from botocore.exceptions import ClientError
import os
import shutil


aws_access_key_id = ''
aws_secret_access_key = ''
bucket_list = []

client = boto3.client(
        's3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
res = client.list_buckets()

for i in res['Buckets']:
    bucket_list.append(i['Name'])


print(bucket_list)