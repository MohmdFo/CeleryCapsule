import time

from celery import shared_task
from celery.utils.log import get_task_logger

from conf.celery.base import app
from conf.log import setup_logging

setup_logging()
task_logger = get_task_logger("application")


@app.task
def say_hi(message):
    time.sleep(5)
    task_logger.info(message)
