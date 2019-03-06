from django.contrib import admin
from . import models


# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    '''图书模型管理类'''
    list_display = ['id','btitle', 'bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hcomment']


'''----------------------AreaInfo管理类相关--start----------------------'''


class AreaStackedInline(admin.StackedInline):
    # 关联子对象
    model = models.AreaInfo
    # 额外编辑子对象个数
    extra = 2


class AreaTabularInline(admin.TabularInline):
    # 关联子对象
    model = models.AreaInfo
    # 额外编辑子对象个数
    extra = 2


class AreaInfoAdmin(admin.ModelAdmin):
    # ----------下面是列表页的配置选项----------
    # 配置每页显示的个数
    list_per_page = 15
    # 顶部编辑选项
    actions_on_top = True
    # 底部编辑选项
    actions_on_bottom = True
    # 配置显示的列选项
    list_display = ['id', 'atitle', 'parent']
    # 配置搜索框
    search_fields = ["atitle"]
    # 配置右侧过滤选项
    list_filter = ['atitle']

    # ----------下面是编辑页的配置选项----------
    # fields 和 fieldsets 两个选项只能用一个
    # fields = ["atitle", "aparent"]
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aparent']})
    )
    # inlines 配置关联子对象
    # inlines = [AreaStackedInline]
    inlines = [AreaTabularInline]

'''----------------------AreaInfo管理类相关--start----------------------'''

# Register your models here.

admin.site.register(models.BookInfo, BookInfoAdmin)
admin.site.register(models.HeroInfo, HeroInfoAdmin)
admin.site.register(models.NewsType)
admin.site.register(models.NewsInfo)
admin.site.register(models.EmployeeBasicInfo)
admin.site.register(models.EmployeeDetailInfo)
admin.site.register(models.AreaInfo, AreaInfoAdmin)
admin.site.register(models.UploadPic)