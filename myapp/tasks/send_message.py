import time

from celery import shared_task

from conf.celery.base import app


@app.task
def say_hi(message):
    time.sleep(5)
    print(message)
