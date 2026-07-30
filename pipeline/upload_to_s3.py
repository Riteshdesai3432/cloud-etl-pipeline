import boto3
from io import StringIO

from config.config import (
    S3_BUCKET,
    S3_PROCESSED_KEY
)


def upload_processed_csv(df):

    print("=" * 50)
    print("UPLOAD TO AMAZON S3")
    print("=" * 50)

    csv_buffer = StringIO()

    df.to_csv(csv_buffer, index=False)

    s3 = boto3.client("s3")

    s3.put_object(
        Bucket=S3_BUCKET,
        Key=S3_PROCESSED_KEY,
        Body=csv_buffer.getvalue()
    )

    print("Processed CSV uploaded successfully.")
    print(f"S3 Location: s3://{S3_BUCKET}/{S3_PROCESSED_KEY}")