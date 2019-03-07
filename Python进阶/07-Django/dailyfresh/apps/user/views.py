from django.shortcuts import render, redirect
from django.urls import reverse
import re
from .models import User
from django.views import View
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from django.http  import HttpResponse


# Create your views here.


class RegisterView(View):
    def get(self, request):
        return render(request, "user/register.html", {})

    def post(self, request):
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
        # 发送激活邮件，激活链接中包含加密的用户信息
        user_info = {"id": new_user.id, "username": new_user.username}
        serializer = Serializer(settings.SECRET_KEY, 3600)
        encryption_str = str(serializer.dumps(user_info))
        # 发送邮件

        # 返回应答，跳转到首页
        return redirect(reverse("goods:index"))


class ActiveView(View):
    '''激活用户类'''
    def get(self, request, active_str):
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            user_info = serializer.loads(active_str)
            user = User.objects.get(id=user_info["id"])
            user.is_active =1
            user.save()
            # 激活成功，去登陆
            return redirect(reverse("user:login"))
        except SignatureExpired as ret:
            return HttpResponse("激活链接已过期")
        except User.DoesNotExist as ret:
            return HttpResponse("非法用户")


class LoginView(View):
    '''用户登陆'''
    def get(self,request):
        return render(request, "user/login.html", {})

    def post(self,request):
        pass


