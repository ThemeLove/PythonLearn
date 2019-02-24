from django.contrib import admin
from .models import BookInfo
from .models import HeroInfo
from .models import NewsType
from .models import NewsInfo
from .models import EmployeeBasicInfo
from .models import EmployeeDetailInfo
from .models import AreaInfo


# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    '''图书模型管理类'''
    list_display = ['id','btitle', 'bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hcomment']


# Register your models here.

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(NewsType)
admin.site.register(NewsInfo)
admin.site.register(EmployeeBasicInfo)
admin.site.register(EmployeeDetailInfo)
admin.site.register(AreaInfo)