# ==============================
# DATA SOURCE
# ==============================

DATA_SOURCE = "s3"      # local or s3

# ==============================
# LOCAL FILE
# ==============================

LOCAL_FILE = "data/raw/employees_large.csv"

# ==============================
# AMAZON S3
# ==============================

S3_BUCKET = "ritesh-data-engineering-2026-943938400719-ap-south-1-an"
S3_KEY = "raw/employees_large.csv"
S3_PROCESSED_KEY = "processed/employees_clean.csv"

# ==============================
# POSTGRESQL
# ==============================

DB_CONFIG = {
    "host": "database-1.chs22egcybw6.ap-south-1.rds.amazonaws.com",
    "port": "5432",
    "database": "data_engineering",
    "user": "postgres",
    "password": "34321234"
}
