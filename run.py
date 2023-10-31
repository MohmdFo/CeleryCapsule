# from tasks import say_hi, app
from conf.celery.base import app
from myapp.tasks import say_hi

say_hi.delay("Hi everyone!!")
