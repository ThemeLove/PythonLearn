from django.shortcuts import render, redirect
from django.urls import reverse
import re
from .models import User, Address
from goods.models import GoodsSKU
from django.views import View
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from django.http  import HttpResponse
from django.contrib.auth import authenticate, login, logout
from celery_tasks import tasks
from utils import mixin
from django_redis import get_redis_connection


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
        # 异步发送邮件,使用celery
        tasks.send_register_active_email.delay(email, username, active_token)
        # 返回应答，跳转到首页
        return redirect(reverse("goods:index"))


class ActiveView(View):
    '''激活用户类'''
    def get(self, request, active_str):
        serializer = Serializer(settings.SECRET_KEY, 3600)
        user = None
        try:
            active_token = serializer.loads(active_str)

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
                next_url = request.GET.get("next", reverse("goods:index"))
                response = redirect(next_url)
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


class LogoutView(View):
    '''退出登录'''
    def get(self, request):
        # 利用django框架自身的logout方法，然后重定向到首页视图
        logout(request)
        return redirect(reverse("goods:index"))


class UserInfoView(mixin.LoginRequiredMixin, View):
    '''用户中心-信息页'''
    def get(self, request):
        # 获取默认收获地址
        address = Address.objects.get_default_address(request.user.id)
        con = get_redis_connection("default")
        history_key = "history_%s" %(request.user.id,)
        sku_id_list = con.lrange(history_key, 0, 4)
        sku_goods = []
        for sku_id in sku_id_list:
            sku_good = GoodsSKU.objects.get(id=sku_id)
            sku_goods.append(sku_good)

        context = {
            "page": "user",
            "address": address,
            "goods": sku_goods
        }

        return render(request, 'user/user_center_info.html', context)


class UserOrderView(mixin.LoginRequiredMixin, View):
    '''用户中心-订单页'''
    def get(self, request):
        # 获取用户的订单信息
        return render(request, 'user/user_center_order.html', {"page": "order"})


class UserSiteView(mixin.LoginRequiredMixin, View):
    '''用户中心-地址页'''
    def get(self, request):
        # 查找该用户的默认收货地址,传递给模板
        try:
            address = Address.objects.get_default_address(user_id=request.user.id)
        except Address.DoesNotExist as e:
            address = None
        return render(request, 'user/user_center_site.html', {"page": "site", "address": address})

    def post(self, request):
        '''添加地址'''
        receiver = request.POST.get("receiver")
        addr = request.POST.get('addr')
        zip_code = request.POST.get("zip_code")
        phone = request.POST.get("phone")

        if not all([receiver, addr, phone]):  # 这里不校验邮箱
            return render(request, 'user/user_center_site.html', {"errormsg": "数据不完整"})

        if not re.match(r"^1[3|4|5|7|8][0-9]{9}$", phone):
            return render(request, 'user/user_center_site.html', {"errormsg": "手机格式不正确"})

        # 添加新邮箱之前先判断该用户是否已有默认邮箱，如果没有将新添加的邮箱作为默认邮箱，否则不作为默认邮箱
        try:
            address = Address.objects.get_default_address(user_id=request.user.id)
        except Address.DoesNotExist as e:
            # 说明该用户尚未添加邮箱
            address = None

        if address:
            is_default = False
        else:
            is_default = True

        Address.objects.create(user_id=request.user.id, receiver=receiver, addr=addr, phone=phone, zip_code=zip_code, is_default=is_default)
        return redirect(reverse("user:site"))  # 重定向的请求方式是get
