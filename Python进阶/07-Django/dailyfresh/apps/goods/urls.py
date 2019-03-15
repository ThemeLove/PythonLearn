from django.urls import path
from . import views

app_name = "goods"
# 通过
urlpatterns = [
    # 通过url函数设置url路由配置项
    # r'^index$'严格匹配开头和结尾
    # path('')
    path("index", views.IndexView.as_view(), name="index"),
    path("", views.IndexView.as_view())

]