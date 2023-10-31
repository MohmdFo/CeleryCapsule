import os
import time

from celery import Celery
from kombu import Queue

app = Celery("tasks", broker="pyamqp://guest:guest@localhost//")

app.conf.update(
    timezone="UTC",
    enable_utc=True,
)


def discover_tasks_modules():
    base_path = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    modules = []

    # Iterate through items in project root
    for item in os.listdir(base_path):
        module_path = os.path.join(base_path, item)
        # Check if item is a directory and has an __init__.py file, making it a module
        if os.path.isdir(module_path) and "__init__.py" in os.listdir(module_path):
            task_path = os.path.join(module_path, "tasks")
            # Check if the tasks submodule exists
            if os.path.exists(task_path) and "__init__.py" in os.listdir(task_path):
                modules.append(f"{item}.tasks")
    return modules


app.autodiscover_tasks(discover_tasks_modules())
