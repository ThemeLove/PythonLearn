from django.template import Library

register = Library()

'''自定义过滤器
1.在应用目录下建立templatetags包目录
2.新建模块，导入from django.template import Library模块 
3.实例化一个register = Library()对象
4.自定义一个过滤器方法
5.用register的filter装饰器装饰过滤器方法
6.在settings.py模块中添加到install_app选项中，比如配置：“booktest.templatetags”
7.模板中使用过滤器时用{% load my_filter%}加载，如果有模板继承，要放到其后面
'''


@register.filter
def mod(value1, value2):
    return value1%value2 == 0
