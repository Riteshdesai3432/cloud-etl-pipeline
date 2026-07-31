# 🚀 Cloud ETL Pipeline using Python, AWS S3, Amazon RDS, Docker & EC2

An end-to-end Cloud ETL (Extract, Transform, Load) pipeline built using **Python**, **Pandas**, **AWS S3**, **Amazon RDS (PostgreSQL)**, **Docker**, and **EC2**.

The pipeline reads employee data from Amazon S3, validates and cleans the data, uploads the cleaned dataset back to S3, and finally loads it into an Amazon RDS PostgreSQL database.

---

# 📌 Project Architecture

```
                 +----------------+
                 |   Amazon S3    |
                 | Raw CSV File   |
                 +-------+--------+
                         |
                         |
                  Extract Data
                         |
                         v
              +--------------------+
              | Python ETL Pipeline|
              +--------------------+
                         |
         +---------------+---------------+
         |                               |
         |                               |
   Validate Data                  Transform Data
         |                               |
         +---------------+---------------+
                         |
                  Cleaned Data
                         |
          +--------------+--------------+
          |                             |
          |                             |
 Upload Clean CSV to S3          Load into Amazon RDS
          |                             |
          +--------------+--------------+
                         |
                         v
                  ETL Completed
```

---

# ✨ Features

- Read CSV file from Amazon S3
- Data Validation
- Data Cleaning & Transformation
- Upload cleaned CSV back to Amazon S3
- Load cleaned data into Amazon RDS PostgreSQL
- Dockerized Application
- Deployable on AWS EC2
- IAM Role based AWS authentication
- Logging support
- Modular project structure

---

# 🛠 Tech Stack

- Python 3.11
- Pandas
- SQLAlchemy
- Psycopg2
- Boto3
- PostgreSQL
- Amazon S3
- Amazon RDS
- AWS EC2
- Docker
- Git & GitHub

---

# 📁 Project Structure

```
cloud-etl-pipeline/

│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── pipeline/
│   ├── extract.py
│   ├── validate.py
│   ├── transform.py
│   ├── upload_to_s3.py
│   ├── load.py
│   ├── logger.py
│   └── __init__.py
│
├── scripts/
│   ├── main.py
│   └── 01_read_from_s3.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ⚙️ ETL Workflow

## 1️⃣ Extract

- Read Employee CSV from Amazon S3
- Load data into Pandas DataFrame

---

## 2️⃣ Validate

Validation checks include:

- Missing Department
- Duplicate Employee Numbers
- Duplicate Rows
- Negative Monthly Income
- Invalid Gender
- Invalid Business Travel
- Invalid Attrition
- Invalid Employee Count
- Invalid Standard Hours
- Invalid Age

---

## 3️⃣ Transform

Cleaning steps:

- Remove duplicate employees
- Handle missing values
- Standardize categorical values
- Save cleaned CSV locally

---

## 4️⃣ Upload

Upload cleaned CSV to:

```
s3://<bucket-name>/processed/employees_clean.csv
```

---

## 5️⃣ Load

Load cleaned data into Amazon RDS PostgreSQL using SQLAlchemy.

---

# ☁ AWS Services Used

## Amazon S3

Used as

- Raw Data Storage
- Processed Data Storage

---

## Amazon EC2

Used to deploy and execute the ETL pipeline.

---

## Amazon RDS

Used to store the final cleaned employee data.

---

## IAM Role

EC2 uses an IAM Role for secure access to S3.

No AWS Access Keys are hardcoded.

---

# 🐳 Docker

Build Docker Image

```bash
docker build -t cloud-etl-pipeline:v1 .
```

Run Container

```bash
docker run --rm cloud-etl-pipeline:v1
```

On EC2

```bash
sudo docker build -t cloud-etl-pipeline:v1 .
```

```bash
sudo docker run --rm cloud-etl-pipeline:v1
```

---

# 🖥 Running Locally

Clone Repository

```bash
git clone https://github.com/Riteshdesai3432/cloud-etl-pipeline.git
```

```bash
cd cloud-etl-pipeline
```

Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Pipeline

```bash
python -m scripts.main
```

---

# ☁ Running on AWS EC2

SSH into EC2

```bash
ssh -i your-key.pem ubuntu@<EC2-Public-IP>
```

Clone Repository

```bash
git clone https://github.com/Riteshdesai3432/cloud-etl-pipeline.git
```

```bash
cd cloud-etl-pipeline
```

Build Docker Image

```bash
sudo docker build -t cloud-etl-pipeline:v1 .
```

Run Container

```bash
sudo docker run --rm cloud-etl-pipeline:v1
```

---

# 📦 Requirements

Install packages

```bash
pip install -r requirements.txt
```

Main Libraries

- pandas
- sqlalchemy
- psycopg2-binary
- boto3

---

# 📊 Sample Output

```
============================================================
EMPLOYEE DATA ETL PIPELINE
============================================================

EXTRACT PHASE

Reading data from S3...

File Loaded Successfully

Rows : 15000

Columns : 35

Validation Report

Missing Department : 300

Duplicate Employees : 98

Negative Monthly Income : 250

TRANSFORM PHASE

Rows After Cleaning : 14902

UPLOAD TO AMAZON S3

Processed CSV uploaded successfully

LOAD PHASE

Data loaded successfully into PostgreSQL.

Rows Loaded : 14902

ETL PIPELINE COMPLETED SUCCESSFULLY
```

---

# 🎯 Skills Demonstrated

- Python Programming
- ETL Development
- Data Validation
- Data Cleaning
- Pandas
- SQLAlchemy
- PostgreSQL
- AWS S3
- Amazon RDS
- Amazon EC2
- IAM Roles
- Docker
- Git
- GitHub
- Linux

---

# 🚀 Future Improvements

- Apache Airflow orchestration
- Apache Spark integration
- AWS Glue support
- CloudWatch logging
- CI/CD using GitHub Actions
- Unit testing
- Data quality dashboard
- Docker Compose
- Kubernetes deployment

---

# 👨‍💻 Author

**Ritesh Desai**

GitHub:
https://github.com/Riteshdesai3432


---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub.