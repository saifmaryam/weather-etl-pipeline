# 🌦️ Weather ETL Pipeline

> An automated, containerized ETL pipeline that pulls live weather data, transforms it, and loads it into PostgreSQL — orchestrated end-to-end with Apache Airflow.

## Why This Project?

Most beginner ETL projects stop at "extract and print." This one goes further — it's a **fully automated, self-scheduling pipeline** that runs independently every hour, complete with monitoring, retry logic, and containerized infrastructure. Built from scratch to understand what actually happens behind the scenes of production data pipelines.

## Architecture

```
OpenWeatherMap API → Extract → Transform → Load → PostgreSQL
                          ↑
                   Apache Airflow
                   (scheduled hourly)
```

Everything runs inside Docker containers — no manual scripts, no forgetting to run a script at 2 AM.

## What It Does

| Stage | What Happens |
|-------|-------------|
| **Extract** | Pulls live weather data for Sialkot from the OpenWeatherMap REST API |
| **Transform** | Cleans raw JSON into structured fields (temp, humidity, wind, description) + adds a timestamp |
| **Load** | Inserts the clean record into a PostgreSQL `weather_data` table |
| **Orchestrate** | Airflow triggers this entire flow automatically, every hour, with logging and retry-on-failure |

## Tech Stack

`Python` · `Docker` · `Docker Compose` · `PostgreSQL` · `Apache Airflow` · `psycopg2` · `python-dotenv`

## Real Problems Solved While Building This

This wasn't a copy-paste tutorial project. Debugging it end-to-end meant working through:
- WSL2 + Docker integration issues on Windows
- Docker volume mounts silently failing (files "existing" locally but invisible inside containers)
- A Windows-style file path breaking a Linux container (`C:\path` vs `/opt/airflow/path`)
- Diagnosing a task that reported "SUCCESS" in Airflow while silently failing underneath — traced back to an expired API key using container logs

Every one of these is a real issue Data Engineers run into — and now I know how to debug them.

## Run It Yourself

```bash
git clone https://github.com/saifmaryam/weather-etl-pipeline.git
cd weather-etl-pipeline
# create a .env file with: WEATHER_API_KEY=your_key_here
docker-compose up -d
```

Airflow UI → `localhost:8080` (default login: admin/admin)

## Author

**Maryam Saif** — [GitHub](https://github.com/saifmaryam)
