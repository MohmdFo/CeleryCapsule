from conf.celery.base import app

argv = [
    "worker",
    "--loglevel=INFO",
    "--pool=solo",
]
app.start(argv)
