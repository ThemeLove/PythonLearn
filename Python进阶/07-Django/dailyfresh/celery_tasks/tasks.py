# django环境的初始化，要在任务处理者一端加上
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dailyfresh.settings')
django.setup()

from celery import Celery
from django.conf import settings
from django.core.mail import send_mail
from goods.models import GoodsType, IndexGoodsBanner, IndexPromotionBanner, IndexTypeGoodsBanner
from django_redis import get_redis_connection
from django.template import loader

# 创建一个Celery类的实例对象
app = Celery('celery_tasks.task', broker='redis://127.0.0.1:6379/8')


# 定义任务函数
@app.task
def send_register_active_email(to_email, username, active_token):
    # 发送邮件
    subject = "天天生鲜激活邮件"
    message = ""
    html_message = "<h1>%s,欢迎您成为天天生鲜注册会员</h1>请点击下面链接激活您的账户</br><a href='http://10.200.202.16:8000/user/active/%s'>http://10.200.202.16:8000/user/active/%s</a>" % (
    username, active_token, active_token)
    sender = settings.EMAIL_FROM
    # sender = "lqsthemelove@163.com"
    # 收件人列表
    receiver = [to_email]

    send_mail(subject, message, sender, receiver, html_message=html_message)


@app.task
def generate_static_index_html():
    def get(self, request):
        # 获取商品的种类信息
        goods_types = GoodsType.objects.all()
        # 获取首页轮播商品信息
        goods_banners = IndexGoodsBanner.objects.all().order_by('index')
        # 获取首页促销活动信息
        promotion_banners = IndexPromotionBanner.objects.all().order_by('index')

        for goods_type in goods_types:
            # 获取type种类首页分类商品的图片展示信息
            image_banners = IndexTypeGoodsBanner.objects.filter(type=goods_type, display_type=1)
            # 获取type种类首页分类商品的文字展示信息
            title_banners = IndexTypeGoodsBanner.objects.filter(type=goods_type, display_type=0)

            # 动态给type增加属性，分别保存首页分类商品的图片展示信息
            goods_type.image_banners = image_banners
            goods_type.title_banners = title_banners

        # 获取用户购物车中商品的数目
        user = request.user
        cart_count = 0
        if user.is_authenticated():
            # 用户已登录
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' % user.id
            cart_count = conn.hlen(cart_key)

        context = {
            'types': goods_types,
            'goods_banners': goods_banners,
            'promotion_banners': promotion_banners,
            'cart_count': cart_count
        }
        # 使用模板
        # 1.加载模板文件，返回模板对象
        temp = loader.get_template('base/static_index.html')
        # 2.定义模板上下文
        # context = RequestContext(request, context)
        # 3.渲染模板w为字符串
        static_index_html = temp.render(context)
        # 4.生成首页对应的静态页面
        save_path = os.path.join(settings.BASE_DIR, 'static/index.html')
        print("save_path=%s"% save_path)
        print("static_index_html="+static_index_html)
        with open(save_path, 'w') as f:
            f.write(static_index_html)
