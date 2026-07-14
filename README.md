# Distributed Task Scheduler with Celery Beat

A Flask application demonstrating scheduled background tasks using Celery Beat.

## Features

- Scheduled task execution
- Background workers
- Redis message broker
- Manual task triggering
- Health endpoint

## Technologies Used

- Python
- Flask
- Celery
- Celery Beat
- Redis

## Installation

```bash
pip install -r requirements.txt
```

## Start Services
Start Redis
docker compose up -d

Start Celery Worker
celery -A tasks worker --loglevel=info

Start Celery Beat
celery -A tasks beat --loglevel=info

Run Flask
python app.py
