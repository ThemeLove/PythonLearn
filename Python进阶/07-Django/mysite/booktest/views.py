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
    if "username" in request.COOKIES:
        username = request.COOKIES.get("username")
    else:
        username = ""
    if "password" in request.COOKIES:
        password = request.COOKIES.get("password")
    else:
        password = ""
    if "remember" in request.COOKIES:
        remember = request.COOKIES.get("remember")
    else:
        remember = "false"
    return render(request, 'booktest/ajax_login.html', {"username": username, "password": password, "remember": remember})


def ajax_check_login(request):
    if request.method == "POST":
        queryDict = request.POST
    else:
        queryDict = request.GET
    username = queryDict.get('username')
    password = queryDict.get('password')
    remember = queryDict.get('remember')

    print("type of remember="+ str(type(remember)))  # str类型
    print("remember=" + remember)

    if username == 'admin' and password == 'themelove':  # 登录成功
        response = JsonResponse({"status": 1, "msg": "登录成功"})
        if remember == "true": # 用户选择记住用户名和密码
            response.set_cookie("username", username, max_age=7*24*3600)
            response.set_cookie("password", password, max_age=7*24*3600)
            response.set_cookie("remember", remember, max_age=7*24*3600)
        else: # 用户没有勾选用户名和密码，要清除cookie
            response.set_cookie("username", "", max_age=0)
            response.set_cookie("password", "", max_age=0)
            response.set_cookie("remember", "false", max_age=0)

        return response
    else:  # 登录失败
        return JsonResponse({"status": 0, "msg": "用户名或密码错误"})


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
