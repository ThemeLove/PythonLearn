from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# 1.定义视图函数，HttpRequest
# 2.进行url配置，建立url地址和视图的对应关系
# http://127.0.0.1:8000/index
def index(request):
    return HttpResponse("day day up")
