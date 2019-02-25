from django.conf.urls import url
from .views import show_books
from .views import book_detail
from .views import add_book
from .views import delete_book
# 通过
urlpatterns = [
    # 通过url函数设置url路由配置项
    # r'^index$'严格匹配开头和结尾
    url(r'^', show_books),
    url(r'^index[/]$', show_books),
    url(r'^books[/]$', show_books),
    url(r'^book/(\d+)/detail[/]$', book_detail),
    url(r'^addbook[/]$', add_book),
    url(r'^deletebook/(\d+)[/]$', delete_book)
]