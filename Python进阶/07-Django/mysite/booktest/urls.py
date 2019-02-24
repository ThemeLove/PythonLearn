from django.conf.urls import url
from .views import index
# 通过
urlpatterns = [
    # 通过url函数设置url路由配置项
    # r'^index$'严格匹配开头和结尾
    url(r'^index[/]$', index)

]