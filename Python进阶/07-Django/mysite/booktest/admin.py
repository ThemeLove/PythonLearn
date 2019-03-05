from django.contrib import admin
from . import models


# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    '''图书模型管理类'''
    list_display = ['id','btitle', 'bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hcomment']


# Register your models here.

admin.site.register(models.BookInfo, BookInfoAdmin)
admin.site.register(models.HeroInfo, HeroInfoAdmin)
admin.site.register(models.NewsType)
admin.site.register(models.NewsInfo)
admin.site.register(models.EmployeeBasicInfo)
admin.site.register(models.EmployeeDetailInfo)
admin.site.register(models.AreaInfo)
admin.site.register(models.UploadPic)