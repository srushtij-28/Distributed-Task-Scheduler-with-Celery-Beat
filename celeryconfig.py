from celery.schedules import crontab

broker_url = "redis://localhost:6379/0"
result_backend = "redis://localhost:6379/0"

beat_schedule = {
    "daily-report": {
        "task": "tasks.generate_report",
        "schedule": crontab(minute="*/1")
    }
}

timezone = "UTC"
