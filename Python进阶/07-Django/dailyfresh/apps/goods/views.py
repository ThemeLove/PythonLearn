from django.shortcuts import render
from django.views import View
from .models import GoodsType, IndexGoodsBanner, IndexPromotionBanner, IndexTypeGoodsBanner
from django_redis import get_redis_connection

# Create your views here.


class IndexView(View):
    '''首页'''
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
        if user.is_authenticated:
            # 用户已登录
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' %user.id
            cart_count = conn.hlen(cart_key)

        context = {
            'types': goods_types,
            'goods_banners': goods_banners,
            'promotion_banners':promotion_banners,
            'cart_count': cart_count
        }
        return render(request, 'base/static_index.html', context)
