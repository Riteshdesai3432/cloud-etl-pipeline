import boto3
import pandas as pd
from io import StringIO

#Create S3 client

s3 = boto3.client("s3")

#Bucket Details

bucket_name = "ritesh-data-engineering-2026-943938400719-ap-south-1-an"
file_key = "raw/employees_large.csv"

#Read file from s3

response = s3.get_object(Bucket=bucket_name,Key=file_key)

#convert bytes to string

csv_content = response["Body"].read().decode("utf-8")

#Read it into pandas

df = pd.read_csv(StringIO(csv_content))

print("=" * 50)
print("FILE READ SUCCESSFULLY FROM AMAZON S3")
print("=" * 50)

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nFirst 5 Rows:")
print(df.head())