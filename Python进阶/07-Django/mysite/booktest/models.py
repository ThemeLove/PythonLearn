from django.db import models
from datetime import datetime


# Create your models here.
class BookInfoManager(models.Manager):
    '''图书类管理器类'''
    # 重写管理器原有的方法
    def all(self):
        books =super().all().filter(isDelete=False)
        return books

    # 添加新方法create_book
    # 注意Manager自带有create方法，这里是添加新方法，不是重写
    def create_book(self, btitle, bpub_date):
        # self.model是Manager里提供的方法可以获取到和Manager关联的模型类
        # BookInfo = self.model
        # book = BookInfo()

        # self.model()直接表示创建一个对象关联模型类对象
        book = self.model()
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        return book


# 图书类
class BookInfo(models.Model):
    '''图书模型类'''
    # CharField说明是一个字符串，max_length指定字符串的最大长度
    btitle = models.CharField(max_length=20)
    # 出版日期， DateField说明是一个日期类型
    bpub_date = models.DateField(default=datetime(1990,1,1))
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)
    # 创建自定义管理器对象替换原生的objects
    objects = BookInfoManager()

    def __str__(self):
        return self.btitle

    # 指定模型类对应的表名，这样创建的表名就不会跟随项目名
    # class Meta:
    #     db_table = 'bookinfo'



class HeroInfo(models.Model):
    '''图书英雄类'''
    # 英雄名称
    hname = models.CharField(max_length=20)
    # 英雄性别，default=True代表男性
    hgender = models.BooleanField(default=True)
    # 评论
    hcomment = models.CharField(max_length=128, null=True, blank=False)
    # 删除标记
    isDelete = models.BooleanField(default=False)
    # 关系属性外键
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.hname


class NewsType(models.Model):
    '''新闻类型类'''
    type_name = models.CharField(max_length=20)


class NewsInfo(models.Model):
    # 新闻标题
    title = models.CharField(max_length=128)
    # 发布时间
    pub_date = models.DateTimeField(auto_now_add=True)
    # 信息内容
    content = models.TextField()
    # 关系属性，代表信息所属的类型
    news_type = models.ManyToManyField('NewsType')



class EmployeeBasicInfo(models.Model):
    '''员工基本信息类'''
    # 姓名
    name = models.CharField(max_length=20)
    # 性别
    gender = models.BooleanField(default=False)
    # 年龄
    age = models.IntegerField()


class EmployeeDetailInfo(models.Model):
    # 联系地址
    addr = models.CharField(max_length=256)
    # 关系属性，代表员工基本信息
    employee_basic = models.OneToOneField('EmployeeBasicInfo', on_delete=models.CASCADE)


class AreaInfo(models.Model):
    '''地区模型类'''
    # 地区名称,第一个参数verbose_name“地区名称”代表在管理后台显示的列标题
    atitle = models.CharField("地区名称", max_length=20)
    # 建立自关联
    aparent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    # 自定义方法
    def parent(self):
        if self.aparent is None:
            return ""
        return self.aparent.atitle
    # 配置自定义方法在管理后台显示的列标题
    parent.short_description = "父级地区名称"
    # 配置自定义方法按照那个字段排序
    parent.admin_order_field = "atitle"

    # 重写__str__方法，管理后台为该类对象时显示的方式
    def __str__(self):
        return self.atitle


class UploadPic(models.Model):
    path = models.ImageField(upload_to='booktest/')
