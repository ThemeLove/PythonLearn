from django.shortcuts import render, redirect
from django.urls import reverse
import re
from .models import User
from django.views import View
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from django.http  import HttpResponse
from django.contrib.auth  import authenticate, login
from django.core.mail import send_mail


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
        active_token = serializer.dumps(user_info).decode('utf8')
        # 发送邮件
        subject = "天天生鲜激活邮件"
        message = ""
        html_message = "<h1>%s,欢迎您成为天天生鲜注册会员</h1>请点击下面链接激活您的账户</br><a href='http://10.200.202.16:8000/user/active/%s'>http://10.200.202.16:8000/user/active/%s</a>" % (username, active_token, active_token)
        sender = settings.EMAIL_FROM
        # 收件人列表
        receiver = [email]

        send_mail(subject, message, sender, receiver, html_message=html_message)

        # 返回应答，跳转到首页
        return redirect(reverse("goods:index"))


class ActiveView(View):
    '''激活用户类'''
    def get(self, request, active_str):
        serializer = Serializer(settings.SECRET_KEY, 3600)
        user = None
        try:
            active_token = serializer.loads(active_str)
            print("active_token="+active_token)
            user = User.objects.get(id=active_token["id"])
            user.is_active = 1
            user.save()
            # 激活成功，去登陆
            return redirect(reverse("user:login"))
        except SignatureExpired as ret:
            print("激活链接已过期")
            return HttpResponse("激活链接已过期")
        except User.DoesNotExist as ret:
            return HttpResponse("非法用户")


class LoginView(View):
    '''用户登陆'''
    def get(self, request):
        if "username" in request.COOKIES:
            username = request.COOKIES.get("username")
            checked = "checked"
        else:
            username = ""
            checked = ""
        return render(request, "user/login.html", {"username": username, "checked": checked})

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        remember = request.POST.get("remember")

        if not all([username, password]):
            return render(request, 'user/login.html', {"errormsg": "账号密码不完整"})

        user = authenticate(username=username, password=password)
        if user is not None:  # 认证成功
            print("username=%s,password=%s, auth success" % (username, password))
            if user.is_active:
                print("username=%s,password=%s, is_active" % (username, password))
                # 没有激活
                login(request, user)
                print("username=%s,password=%s, login" % (username, password))
                response = redirect(reverse("goods:index"))
                if remember == "on":
                    response.set_cookie("username", username, max_age=7*24*3600)
                else:
                    response.delete_cookie("username")
                return response
            else:
                # 没有激活
                return render(request, "user/login.html", {"errormsg": "账号未激活"})
        else:  # 认证失败
            print("username=%s,password=%s, 账号密码错误" %(username, password))
            return render(request, 'user/login.html', {"errormsg": "账号或密码错误"})



