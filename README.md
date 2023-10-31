# Celery Modularity in Pure Python

This project demonstrates how to set up and modularize a Celery project using pure Python. The architecture is designed for scalable additions of tasks and easy configuration management.

## Structure

The project has a clear separation of concerns, splitting the configuration, task definitions, and execution scripts.

```bash
- myapp               # Module for task definitions
    |
    |__init__.py
    |tasks/          
        |__init__.py
        |send_message.py   # Sample task

- conf                # Configuration module
    |
    |__init__.py
    |celery/
        |__init__.py
        |base.py         # Core Celery configuration

- run.py              # Script to run tasks
- worker.py       # Script to initiate the Celery worker
```

## Configuration (`conf.celery.base`)

The central configuration for Celery resides in `conf.celery.base`. It sets up the broker, timezone, and other necessary parameters. This modular approach allows for centralized management of configurations.

The configuration utilizes the `autodiscover_tasks` method to automatically discover tasks within the specified modules, ensuring that adding new tasks is seamless.

## Running Tasks

To execute a Celery task:

```bash
python run.py
```

This script imports a sample task from `myapp.tasks` and runs it.

## Running the Celery Worker

To start the Celery worker, use:

```bash
python worker.py
```

This will initiate the Celery worker with the configurations defined in `conf.celery.base`.

## Conclusion

This project offers a blueprint for setting up a modular Celery architecture in a Python application. By separating configurations, task definitions, and run scripts, it provides a scalable and maintainable structure for Celery-based applications.
