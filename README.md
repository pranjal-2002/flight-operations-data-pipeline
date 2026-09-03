# ✈️ Flight Operations Data Pipeline

An end-to-end data engineering project that extracts real-time flight data, transforms and validates it, loads it into PostgreSQL, and visualizes the data using Power BI.

## 🏗️ Architecture

OpenSky Network API
        ↓
Apache Airflow
        ↓
Extract → Transform → Validate → Load
        ↓
PostgreSQL
        ↓
Power BI Dashboard

## 🛠️ Technologies

- Python
- Apache Airflow
- PostgreSQL
- Pandas
- Docker
- REST API
- SQL
- Power BI

## 📂 Project Structure

```text
flight-operations-data-pipeline/
│
├── dags/
│   └── flight_pipeline_dag.py
│
├── scripts/
│   ├── config.py
│   ├── db.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── logger.py
│   └── validation.py
│
├── sql/
│   └── create_table.sql
│
├── dashboard/
│   └── Flight_Operation_Report.pbix
│
├── images/
│
├── .env.example
├── .gitignore
├── docker-compose.yaml
├── requirements.txt
└── README.md