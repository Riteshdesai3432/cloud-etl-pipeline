# 🚀 Employee Data ETL Pipeline

A production-style ETL (Extract, Transform, Load) pipeline built using **Python**, **Pandas**, and **PostgreSQL**.

This project demonstrates how employee data can be extracted from a CSV file, validated, cleaned, transformed, and loaded into a PostgreSQL database.

---

# 📌 Project Overview

The pipeline performs the following tasks:

- 📥 Extract employee data from CSV
- ✅ Validate data quality
- 🧹 Clean and transform data
- 💾 Save cleaned data
- 🐘 Load data into PostgreSQL
- 📝 Generate execution logs

---

# 🏗️ ETL Architecture

```
                 employees_large.csv
                         │
                         ▼
                 Extract Module
                         │
                         ▼
                Validation Module
                         │
                         ▼
               Transformation Module
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
    employees_clean.csv      PostgreSQL Database
                                     │
                                     ▼
                              Execution Logs
```

---

# 🛠️ Tech Stack

- Python 3.11
- Pandas
- PostgreSQL
- SQLAlchemy
- psycopg2
- python-dotenv

---

# 📂 Project Structure

```
employee-data-etl-pipeline/

│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── data/
│   ├── raw/
│   │   └── employees_large.csv
│   │
│   └── processed/
│       └── employees_clean.csv
│
├── logs/
│
├── pipeline/
│   ├── __init__.py
│   ├── extract.py
│   ├── validate.py
│   ├── transform.py
│   ├── load.py
│   └── logger.py
│
├── scripts/
│   └── main.py
│
├── sql/
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ⚙️ Features

### Extract

- Reads CSV files
- Handles file loading errors

### Validate

- Missing values detection
- Duplicate employee detection
- Invalid values checking
- Data quality report generation

### Transform

- Remove duplicate employees
- Fill missing departments
- Remove invalid records
- Add Bonus column
- Add Salary Category
- Add Experience Level

### Load

- Load cleaned data into PostgreSQL
- Replace existing table
- Verify successful loading

### Logging

- Records ETL execution
- Stores execution logs

---

# 📊 Data Quality Checks

The pipeline validates:

- Missing Department
- Duplicate Employee Number
- Negative Monthly Income
- Invalid Gender
- Invalid Business Travel
- Invalid Attrition
- Invalid Employee Count
- Invalid Standard Hours
- Invalid Age

---

# ▶️ How to Run

## 1. Clone Repository

```bash
git clone <repository-url>
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Configure Environment

Create a `.env` file:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=data_engineering
DB_USER=postgres
DB_PASSWORD=your_password
```

## 4. Run the Pipeline

```bash
python scripts/main.py
```

---

# 📈 Sample Output

```
========================================================
EMPLOYEE DATA ETL PIPELINE
========================================================

Extract Phase Completed

Validation Completed

Transformation Completed

Data Loaded Successfully

Rows Loaded : 14902

ETL Pipeline Completed Successfully
```

---

# 📊 Skills Demonstrated

- ETL Pipeline Development
- Python Programming
- Pandas Data Processing
- PostgreSQL
- SQLAlchemy
- Data Cleaning
- Data Validation
- Logging
- Project Structure
- Environment Configuration

---

# 🚀 Future Improvements

- Apache Airflow Integration
- AWS S3 Support
- Docker Containerization
- Apache Spark Processing
- Kafka Streaming
- Unit Testing
- CI/CD Pipeline

---

# 👨‍💻 Author

**Ritesh Desai**

Aspiring Data Engineer

---