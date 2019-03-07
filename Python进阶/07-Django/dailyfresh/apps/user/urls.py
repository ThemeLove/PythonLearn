from django.urls import path,re_path
from . import views
app_name = "user"
# 通过
urlpatterns = [
    # 通过url函数设置url路由配置项
    # r'^index$'严格匹配开头和结尾
    # path('')
    path('register', views.register, name="register"),
    path('register_handle', views.register_handle, name='register_handle'),

]