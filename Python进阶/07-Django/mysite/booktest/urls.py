from django.conf.urls import url
from . import views
app_name = 'booktest'
# 通过
urlpatterns = [
    # 通过url函数设置url路由配置项
    # r'^index$'严格匹配开头和结尾
    url(r'^$', views.show_books),
    url(r'^index[/]$', views.show_books, name="index"),
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
    url(r'^get_session$', views.get_all_session),

    # ------------------模板继承--部分--------------
    url(r'^child$', views.inherit_child),
    # ------------------模板注释--部分--------------
    url(r'^comment$', views.comment_test),
    # ------------------模板转义--部分--------------
    url(r'^escape$', views.escape_test),
    # ------------------图片验证码--部分--------------
    url(r'^verifycode', views.verify_code),
    # ------------------反向解析--部分--------------
    url(r'^reverse$', views.reverse_test),
    # ------------------静态文件--部分--------------
    url(r'^static$', views.static_test),
    # ------------------上传文件--部分--------------
    url(r'^upload$', views.show_upload),
    url(r'^upload_handle$', views.upload_handle),
    url(r'^pics$', views.show_pics),
    # ------------------分页--部分--------------
    url(r'^provinces', views.show_provinces),
    url(r'^areas$', views.show_areas),
    url(r'^get_areas', views.get_areas)
]