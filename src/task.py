import os
import time

from celery import Celery

BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379/0")
RESULT_BACKEND = os.environ.get("CELERY_BACKEND", "redis://redis:6379/0")

celery = Celery(__name__, backend=RESULT_BACKEND, broker=BROKER_URL)

@celery.task(name="create_task")
def create_task(task_type):
    time.sleep(task_type)
    return True
