from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from .models import BookInfo

# Create your views here.


# 1.定义视图函数，HttpRequest
# 2.进行url配置，建立url地址和视图的对应关系
# http://127.0.0.1:8000/books对应的函数为show_books
def show_books(request):
    '''显示所有书籍的名字'''
    books = BookInfo.objects.all()
    return render(request, "booktest/show_books.html", {"books": books})


def book_detail(request, bookid):
    book = BookInfo.objects.get(id=bookid)
    heros = book.heroinfo_set.all()
    return render(request, "booktest/book_detail.html", {"book": book, "heros": heros})


def add_book(request):
    '''添加新的书籍'''
    newbook = BookInfo()
    newbook.btitle = "流星蝴蝶剑"
    newbook.save()
    return redirect('/books')


def delete_book(request, bookid):
    book = BookInfo.objects.get(id=bookid)
    book.delete()
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
