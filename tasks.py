from celery import Celery

celery = Celery("tasks")
celery.config_from_object("celeryconfig")

@celery.task
def generate_report():

    print("Generating report...")

    return "Report Generated"
