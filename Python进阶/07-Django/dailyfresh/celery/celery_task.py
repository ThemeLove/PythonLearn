from celery import Celery


# 创建一个Celery类的实例对象
Celery('celery.celery_task', broker=)