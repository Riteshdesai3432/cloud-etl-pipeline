# ☁️ Cloud ETL Pipeline using AWS S3, PostgreSQL & Python

## 📌 Project Overview

This project is an end-to-end Cloud ETL (Extract, Transform, Load) Pipeline built using Python and AWS services. It extracts employee data from an Amazon S3 bucket, validates and cleans the data using Pandas, uploads the processed CSV back to Amazon S3, and loads the cleaned data into PostgreSQL.

The project demonstrates how cloud-based ETL pipelines are built in production environments using AWS.

---

## 🏗️ Architecture

```
                Amazon S3
          (Raw Employee CSV)
                   │
                   ▼
          Extract using boto3
                   │
                   ▼
        Validate & Transform
             (Pandas)
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
 Amazon S3              PostgreSQL
Processed CSV          Cleaned Data
```

---

## 🚀 Features

* Read CSV files directly from Amazon S3
* Validate data quality
* Remove duplicate employee records
* Handle missing values
* Validate categorical columns
* Clean invalid salary values
* Upload cleaned CSV to Amazon S3
* Load processed data into PostgreSQL
* Modular ETL architecture
* Logging support
* Configuration using environment variables

---

## 🛠️ Technologies Used

### Programming

* Python 3.11+

### Python Libraries

* pandas
* boto3
* psycopg2-binary
* python-dotenv

### AWS Services

* Amazon S3
* IAM
* EC2 (Deployment)
* AWS CLI

### Database

* PostgreSQL

---

## 📁 Project Structure

```
cloud-etl-pipeline/
│
├── config/
│   └── config.py
│
├── pipeline/
│   ├── extract.py
│   ├── validate.py
│   ├── transform.py
│   ├── upload_to_s3.py
│   ├── load.py
│   └── logger.py
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
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ ETL Workflow

### 1️⃣ Extract

* Read employee dataset from Amazon S3
* Load data into a Pandas DataFrame

### 2️⃣ Validate

* Check missing values
* Check duplicate records
* Validate categorical columns
* Validate salary values

### 3️⃣ Transform

* Remove duplicate employee records
* Clean invalid values
* Prepare clean dataset

### 4️⃣ Load

* Upload cleaned CSV to Amazon S3
* Load cleaned data into PostgreSQL

---

## ▶️ Running the Project

### Clone Repository

```bash
git clone https://github.com/Riteshdesai3432/cloud-etl-pipeline.git
cd cloud-etl-pipeline
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file and configure:

```
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=
```

### Run

```bash
python scripts/main.py
```

---

## 📊 Sample Output

```
EXTRACT PHASE
✔ Reading data from Amazon S3

VALIDATION PHASE
✔ Missing Values Checked
✔ Duplicate Employees Removed

TRANSFORM PHASE
✔ Data Cleaned Successfully

LOAD PHASE
✔ Uploaded Clean CSV to Amazon S3
✔ Loaded Data into PostgreSQL

ETL PIPELINE COMPLETED SUCCESSFULLY
```

---

## 📸 Screenshots

Add screenshots here after deployment:

* Amazon S3 Bucket
* EC2 Instance
* PostgreSQL Tables
* ETL Execution Output

---

## 📈 Future Improvements

* Amazon RDS PostgreSQL
* Apache Airflow Orchestration
* Docker Containerization
* AWS Lambda
* AWS Glue
* Amazon Athena
* Terraform
* CI/CD using GitHub Actions

---

## 👨‍💻 Author

**Ritesh Desai**

GitHub: https://github.com/Riteshdesai3432
