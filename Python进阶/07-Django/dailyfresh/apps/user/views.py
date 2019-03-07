from django.shortcuts import render, redirect
from django.urls import reverse
import re
from .models import User
import logging


# Create your views here.


def register(request):
    '''注册页面'''
    logging.info("-----register----")
    print("-----register----")
    return render(request, "user/register.html", {})


def register_handle(request):
    # 1.接收参数
    logging.info("-----register_handle----")
    print("-----register_handle----")

    if request.method != "POST":
        return render(request, 'user/register.html', {'errormsg': '请用post方式提交数据'})

    username = request.POST.get('user_name')
    pwd = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')
    # 2.校验参数
    if not all([username, pwd, email, all, allow]):
        return render(request, "user/register.html", {"errormsg": "数据不完整"})
    # 检验邮箱
    if not re.match(r"^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", email):
        return render(request, 'user/register.html', {"errormsg": "邮箱格式不正确"})
    # 校验协议
    if allow != "on":
        return render(request, 'user/register.html', {'errormsg': '请先勾选协议'})

    # 校验用户名是否重复
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        # 用户名不存在
        user = None
    if user:
        # 用户名已存在
        return render(request, "user/register.html", {"errormsg": "用户名已存在"})

    # 3.进行业务处理：进行用户注册
    new_user = User.objects.create_user(username, email, pwd)
    new_user.is_active = 0  # create_user创建的用户默认激活了用户，这里改为不激活
    new_user.save()
    # 返回应答，跳转到首页
    return redirect(reverse("goods:index"))


