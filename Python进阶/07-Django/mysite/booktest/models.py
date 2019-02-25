from django.db import models
from datetime import datetime


# Create your models here.
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

    def __str__(self):
        return self.btitle


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
    # 地区名称
    atitle = models.CharField(max_length=20)
    # 建立自关联
    aparent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)