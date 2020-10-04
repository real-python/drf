import logging
import boto3
from botocore.exceptions import ClientError
import os
import shutil
import uuid


def my_upload(my_file_path):
    bucket_name = 'kuntal12345'
    file_name = my_file_path
    aws_access_key_id = ''
    aws_secret_access_key = ''

    try:
        client = boto3.client(
            's3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        response = client.upload_file(
            file_name, bucket_name, file_name, ExtraArgs={'ACL': 'public-read'})
    
        response = client.generate_presigned_url(
            'get_object', Params={
                'Bucket': bucket_name,
                'Key': file_name
            }, 
            ExpiresIn=3600*2
        )
        os.remove(my_file_path)
        # shutil.rmtree(my_file_path.split('/')[0])
        return response
    except ClientError as e:
        logging.error(e)
        return None