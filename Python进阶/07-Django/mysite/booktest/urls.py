from django.conf.urls import url
from .views import index
from .views import show_books
from .views import book_detail
# 通过
urlpatterns = [
    # 通过url函数设置url路由配置项
    # r'^index$'严格匹配开头和结尾
    url(r'^index[/]$', index),
    url(r'^books$', show_books),
    url(r'^book/(\d+)/detail$', book_detail)
]