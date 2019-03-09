from celery import Celery
from django.conf import settings
from django.core.mail import send_mail

# django环境的初始化，要在任务处理者一端加上
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dailyfresh.settings')
django.setup()

# 创建一个Celery类的实例对象
app = Celery('celery_tasks.task', broker='redis://127.0.0.1:6379/8')


# 定义任务函数
@app.task
def send_register_active_email(to_email, username, active_token):
    # 发送邮件
    subject = "天天生鲜激活邮件"
    message = ""
    html_message = "<h1>%s,欢迎您成为天天生鲜注册会员</h1>请点击下面链接激活您的账户</br><a href='http://10.200.202.16:8000/user/active/%s'>http://10.200.202.16:8000/user/active/%s</a>" % (
    username, active_token, active_token)
    sender = settings.EMAIL_FROM
    # sender = "lqsthemelove@163.com"
    # 收件人列表
    receiver = [to_email]

    send_mail(subject, message, sender, receiver, html_message=html_message)
