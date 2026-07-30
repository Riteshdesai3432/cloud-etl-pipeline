import pandas as pd
import boto3
from io import StringIO

from config.config import (
    DATA_SOURCE,
    LOCAL_FILE,
    S3_BUCKET,
    S3_KEY
)


def extract_data():

    print("=" * 50)
    print("EXTRACT PHASE")
    print("=" * 50)

    # Read from Local CSV
    if DATA_SOURCE == "local":

        print("Reading data from Local File...")

        df = pd.read_csv("LOCAL_FILE")

    # Read from Amazon S3
    elif DATA_SOURCE == "s3":

        print("Reading data from S3...")

        s3 = boto3.client("s3")

        response = s3.get_object(
            Bucket=S3_BUCKET,
            Key=S3_KEY
        )

        csv_data = response["Body"].read().decode("utf-8")

        df = pd.read_csv(StringIO(csv_data))

    else:
        raise ValueError("Invalid DATA_SOURCE. Use 'local' or 's3'.")

    print("File Loaded Successfully")
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    return df