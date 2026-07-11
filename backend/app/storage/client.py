import boto3
from botocore.exceptions import ClientError

from app.core.config import settings

s3_client = boto3.client(
    "s3",
    endpoint_url=settings.S3_ENDPOINT,
    aws_access_key_id=settings.S3_ACCESS_KEY,
    aws_secret_access_key=settings.S3_SECRET_KEY,
    region_name=settings.S3_REGION,
)


def bucket_exists(bucket_name: str) -> bool:
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        return True
    except ClientError:
        return False
