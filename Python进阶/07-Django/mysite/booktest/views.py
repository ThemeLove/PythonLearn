from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, QueryDict, JsonResponse
from django.template import loader, RequestContext
from .models import BookInfo
from datetime import date
import logging


# Create your views here.
def ajax_test(request):
    return render(request, 'booktest/ajax_test.html')


def ajax_hander(request):
    return JsonResponse({"status": 1, "msg": "提示信息"})


def login(request):
    return render(request, "booktest/login.html", {})


def check_login(request):
    if request.method == "POST":
        queryDict = request.POST
    else:
        queryDict = request.GET
    username = queryDict.get('username')
    password = queryDict.get('password')

    if username == 'admin' and password == 'themelove':  # 登录成功
        return redirect('/index')
    else:  # 登录失败
        return redirect('/login')


def ajax_login(request):
    return render(request, 'booktest/ajax_login.html', {})


def ajax_check_login(request):
    if request.method == "POST":
        queryDict = request.POST
    else:
        queryDict = request.GET
    username = queryDict.get('username')
    password = queryDict.get('password')

    if username == 'admin' and password == 'themelove':  # 登录成功
        return JsonResponse({"status":1,"msg":"登录成功"})
    else:  # 登录失败
        return JsonResponse({"status":0, "msg":"用户名或密码错误"})


# 1.定义视图函数，HttpRequest
# 2.进行url配置，建立url地址和视图的对应关系
# http://127.0.0.1:8000/books对应的函数为show_books
def show_books(request):
    '''显示所有书籍的名字'''
    books = BookInfo.objects.all()
    logging.info("show_books")
    return render(request, "booktest/show_books.html", {"books": books})


def book_detail(request, bookid):
    book = BookInfo.objects.get(id=bookid)
    heros = book.heroinfo_set.all()
    logging.info("book_detail:bookid=" + bookid)
    return render(request, "booktest/book_detail.html", {"book": book, "heros": heros})


def add_book(request):
    '''添加新的书籍'''
    newbook = BookInfo()
    newbook.btitle = "流星蝴蝶剑"
    newbook.save()
    logging.info("add_book")
    return redirect('/books')


def delete_book(request, bookid):
    book = BookInfo.objects.get(id=bookid)
    book.delete()
    logging.info("delete_book:bookid="+bookid)
    # book.save()
    return redirect('/books')


def my_render(request, template_path, dict_data):
    '''自己定义的my_render函数，django的loader模块里已经有一个render函数了'''
    # 1.加载模板文件
    template = loader.get_template(template_path)
    # 2.定义模板上下文：给模板文件传递数据
    # context = RequestContext(request, dict_data)
    # 3.模板渲染：产生标准的html内容
    res_html = template.render(dict_data, request)
    return HttpResponse(res_html)
