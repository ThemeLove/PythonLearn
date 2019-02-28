from django.conf.urls import url
from . import views
# 通过
urlpatterns = [
    # 通过url函数设置url路由配置项
    # r'^index$'严格匹配开头和结尾
    url(r'^$', views.show_books),
    url(r'^index[/]$', views.show_books),
    url(r'^books[/]$', views.show_books),
    url(r'^book/(\d+)/detail[/]$', views.book_detail),
    url(r'^addbook[/]$', views.add_book),
    url(r'^deletebook/(\d+)[/]$', views.delete_book),
    url(r'^login$', views.login),
    url(r'^check_login$', views.check_login),

    url(r'^ajax_login$', views.ajax_login),
    url(r'^ajax_check_login$', views.ajax_check_login),

    url(r'^ajax_test$', views.ajax_test),
    url(r'^ajax_handle$', views.ajax_hander),

    url(r'^set_cookie$', views.set_cookie),
    url(r'^get_cookie$', views.get_all_cookie),

    url(r'^set_session$', views.set_session),
    url(r'^get_session$', views.get_all_session)
]