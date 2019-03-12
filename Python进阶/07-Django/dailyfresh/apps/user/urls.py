from django.urls import path,re_path
from . import views

app_name = "user"
# 通过
urlpatterns = [
    path('register', views.RegisterView.as_view(), name="register"),  # 注册用户
    path('active/<str:active_str>', views.ActiveView.as_view(), name="active"),  # 激活用户
    path('login', views.LoginView.as_view(), name='login'),  # 用户登陆
    path('logout', views.LogoutView.as_view(), name='logout'),  # 退出登录
    path('order', views.UserOrderView.as_view(), name='order'),  # 用户中心-订单
    path('site', views.UserSiteView.as_view(), name='site'),  # 用户中心-地址
    path('', views.UserInfoView.as_view(), name='user'),  # 用户中心
]
