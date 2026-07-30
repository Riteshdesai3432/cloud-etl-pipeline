# 🚀 Cloud ETL Pipeline using Python, AWS S3, EC2 & Amazon RDS

## 📌 Project Overview

This project is an end-to-end **Cloud ETL (Extract, Transform, Load) Pipeline** built using **Python**, **Pandas**, **AWS S3**, **Amazon EC2**, and **Amazon RDS PostgreSQL**.

The pipeline reads raw employee data from an Amazon S3 bucket, validates and cleans the data using Pandas, uploads the cleaned dataset back to Amazon S3, and finally loads the processed data into an Amazon RDS PostgreSQL database.

The entire ETL application is deployed and executed on an **Amazon EC2 Ubuntu instance**, making it a cloud-native data engineering project.

---

# 🏗️ Architecture

```text
                Amazon S3
         (employees_large.csv)
                    │
                    ▼
        Amazon EC2 (Ubuntu Linux)
          Python ETL Pipeline
                    │
     Extract → Validate → Transform
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
 Amazon S3                 Amazon RDS
Processed CSV        PostgreSQL Database
employees_clean.csv   employees_clean Table
```

---

# ✨ Features

* Read raw CSV data from Amazon S3
* Validate dataset quality
* Remove duplicate employee records
* Detect missing and invalid values
* Clean and transform data using Pandas
* Save cleaned CSV locally
* Upload cleaned CSV back to Amazon S3
* Load cleaned data into Amazon RDS PostgreSQL
* Logging for every ETL stage
* Modular project structure
* Deployable on Amazon EC2

---

# 🛠️ Tech Stack

### Programming

* Python 3
* Pandas
* SQLAlchemy
* boto3
* psycopg2
* python-dotenv

### AWS Services

* Amazon S3
* Amazon EC2
* Amazon RDS (PostgreSQL)
* IAM Roles
* AWS CLI

### Database

* PostgreSQL

### Tools

* Git
* GitHub
* Ubuntu Linux

---

# 📂 Project Structure

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
│   ├── load.py
│   ├── upload_to_s3.py
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
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔄 ETL Workflow

### Extract

* Read employee CSV from Amazon S3
* Load into a Pandas DataFrame

### Validate

Checks include:

* Missing Departments
* Duplicate Employee IDs
* Duplicate Rows
* Negative Salary Values
* Invalid Gender
* Invalid Business Travel
* Invalid Employee Count
* Invalid Standard Hours
* Invalid Age

### Transform

* Remove duplicate employee records
* Clean invalid values
* Save cleaned CSV locally

### Upload

* Upload processed CSV to Amazon S3

### Load

* Load cleaned dataset into Amazon RDS PostgreSQL using SQLAlchemy

---

# ☁️ AWS Services Used

## Amazon S3

* Store raw employee dataset
* Store cleaned dataset

## Amazon EC2

* Host the ETL application
* Execute the complete pipeline
* Run Ubuntu Linux environment

## Amazon RDS

* Store processed employee data
* PostgreSQL managed by AWS

## IAM Role

* Securely access S3 without storing AWS Access Keys

---

# ▶️ How to Run

Clone the repository

```bash
git clone https://github.com/Riteshdesai3432/cloud-etl-pipeline.git
```

Move into the project

```bash
cd cloud-etl-pipeline
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure your AWS S3 bucket and PostgreSQL database in `config/config.py`.

Run the ETL pipeline

```bash
python -m scripts.main
```

---

# 📊 Sample Output

```
EXTRACT PHASE
✔ File Loaded Successfully

VALIDATION PHASE
✔ Validation Completed

TRANSFORM PHASE
✔ Duplicate Records Removed

UPLOAD TO AMAZON S3
✔ Processed CSV Uploaded Successfully

LOAD PHASE
✔ Data Loaded into Amazon RDS PostgreSQL

ETL PIPELINE COMPLETED SUCCESSFULLY
```

---

# 📚 Skills Demonstrated

* ETL Pipeline Development
* Python Programming
* Pandas Data Processing
* PostgreSQL
* SQLAlchemy
* AWS S3
* Amazon EC2
* Amazon RDS
* IAM Roles
* Linux
* Git & GitHub
* Cloud Deployment

---

# 🚀 Future Improvements

* Dockerize the application
* Schedule ETL using Apache Airflow
* Process streaming data using Apache Kafka
* Process large datasets using Apache Spark (PySpark)
* Add CloudWatch monitoring and alerts
* CI/CD using GitHub Actions

---

# 👨‍💻 Author

**Ritesh Desai**

GitHub: https://github.com/Riteshdesai3432
