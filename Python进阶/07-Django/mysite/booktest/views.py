from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, QueryDict, JsonResponse
from django.template import loader, RequestContext
from .models import BookInfo, UploadPic
from PIL import Image,ImageDraw,ImageFont
from django.utils.six import BytesIO
import logging
from django.conf import settings
from . import models
from django.core.paginator import Paginator


def login_required(view_func):
    '''登录判断装饰器'''
    def wrapper(request, *view_args, **view_kwargs):
        if request.session.has_key('islogin'):
            # 用户已登录，调用对应的视图
            return view_func(request, *view_args, **view_kwargs)
        else:
            # 用户未登录，跳转到登录页
            return redirect('/ajax_login')
    return wrapper


# Create your views here.
def set_cookie(request):
    '''设置cookie'''
    response = JsonResponse({"cookietest":"cookietest"})
    response.set_cookie("cookietest", "cookietest", max_age=3*24*3600)
    return response


def get_all_cookie(request):
    '''获取携带的所有cookie'''
    cookie_dict = dict()
    print("type of request.COOKIES="+ str(type(request.COOKIES)))
    for cookie in request.COOKIES:
        cookie_dict[cookie] = request.COOKIES.get(cookie)
    return JsonResponse({"all_cookie": cookie_dict})


def set_session(request):
    '''设置session'''
    request.session['sessiontest'] = "sessiontest"
    return JsonResponse({'sessiontest':"sessiontest"})


def get_all_session(request):
    print("type of request="+ str(type(request)))
    # request = HttpRequest()
    # session_dict = dict()
    # print("type of session="+ str(type(request.session)))
    # request.
    # for session in request.session:
    #     session_dict[session] = request.session[session]
    sessiontest = request.session['sessiontest']
    return JsonResponse({'all_session': sessiontest})


def ajax_test(request):
    return render(request, 'booktest/ajax_test.html')


def ajax_hander(request):
    return JsonResponse({"status": 1, "msg": "提示信息"})


def login(request):
    return render(request, "booktest/login.html", {})


def check_login(request):
    if request.method == "POST":
        queryDict = request.POST
    else:
        queryDict = request.GET
    username = queryDict.get('username')
    password = queryDict.get('password')

    if username == 'admin' and password == 'themelove':  # 登录成功
        return redirect('/index')
    else:  # 登录失败
        return redirect('/login')


def ajax_login(request):
    # 1.首先根据session判断该用户是否已经登录
    if request.session.get('islogin', "false") == "true":
        return redirect("/index")

    # 2.如果需要重写登录，则根据cookie来判断是否要记住用户名密码来复显用户名密码
    if "username" in request.COOKIES:
        username = request.COOKIES.get("username")
    else:
        username = ""
    if "password" in request.COOKIES:
        password = request.COOKIES.get("password")
    else:
        password = ""
    if "remember" in request.COOKIES:
        remember = request.COOKIES.get("remember")
    else:
        remember = "false"
    return render(request, 'booktest/ajax_login.html', {"username": username, "password": password, "remember": remember})


def ajax_check_login(request):
    if request.method == "POST":
        queryDict = request.POST
    else:
        queryDict = request.GET
    username = queryDict.get('username')
    password = queryDict.get('password')
    remember = queryDict.get('remember')

    print("type of remember="+ str(type(remember)))  # str类型
    print("remember=" + remember)

    if username == 'admin' and password == 'themelove':  # 登录成功
        response = JsonResponse({"status": 1, "msg": "登录成功"})
        request.session['islogin'] = 'true'
        request.session.set_expiry(60)  # 设置过期时间为60秒
        if remember == "true":  # 用户选择记住用户名和密码
            response.set_cookie("username", username, max_age=7*24*3600)
            response.set_cookie("password", password, max_age=7*24*3600)
            response.set_cookie("remember", remember, max_age=7*24*3600)
        else:  # 用户没有勾选用户名和密码，要清除cookie
            response.set_cookie("username", "", max_age=0)
            response.set_cookie("password", "", max_age=0)
            response.set_cookie("remember", "false", max_age=0)

        return response
    else:  # 登录失败
        return JsonResponse({"status": 0, "msg": "用户名或密码错误"})


# 1.定义视图函数，HttpRequest
# 2.进行url配置，建立url地址和视图的对应关系
# http://127.0.0.1:8000/books对应的函数为show_books
@login_required
def show_books(request):
    '''显示所有书籍的名字'''
    books = BookInfo.objects.all()
    logging.info("show_books")
    return render(request, "booktest/show_books.html", {"books": books})


def book_detail(request, bookid):
    book = BookInfo.objects.get(id=bookid)
    heros = book.heroinfo_set.all()
    logging.info("book_detail:bookid=" + bookid)
    return render(request, "booktest/book_detail.html", {"book": book, "heros": heros})


def add_book(request):
    '''添加新的书籍'''
    newbook = BookInfo()
    newbook.btitle = "流星蝴蝶剑"
    newbook.save()
    logging.info("add_book")
    return redirect('/books')


def delete_book(request, bookid):
    book = BookInfo.objects.get(id=bookid)
    book.delete()
    logging.info("delete_book:bookid="+bookid)
    # book.save()
    return redirect('/books')


def my_render(request, template_path, dict_data):
    '''自己定义的my_render函数，django的loader模块里已经有一个render函数了'''
    # 1.加载模板文件
    template = loader.get_template(template_path)
    # 2.定义模板上下文：给模板文件传递数据
    # context = RequestContext(request, dict_data)
    # 3.模板渲染：产生标准的html内容
    res_html = template.render(dict_data, request)
    return HttpResponse(res_html)

# ---------------------下面是--模板继承--测试部分------------------'''


def inherit_child(request):

    books = BookInfo.objects.all()
    return render(request, "booktest/inherit_child.html", {"books": books})

# ---------------------下面是--注释--测试部分------------------'''


def comment_test(request):
    return render(request, "booktest/comment_test.html",{})

# ---------------------下面是--转义--测试部分------------------'''


def escape_test(request):
    book = BookInfo.objects.all().get(id=1)
    return render(request, "booktest/escape_test.html", {"title": "<h1>hello django</h1>"})

# ---------------------下面是--转义--测试部分------------------'''


def verify_code(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    buf = BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

# ---------------------下面是--转义--测试部分------------------'''


def reverse_test(request):
    return render(request, "booktest/reverse_test.html", {})

# ---------------------下面是--静态文件--测试部分------------------'''


def static_test(request):
    return render(request, 'booktest/static_test.html', {})


# ---------------------下面是--上传图片--测试部分------------------'''
def show_upload(request):
    return render(request, 'booktest/show_upload.html', {})


def upload_handle(request):
    # 获取上传的图片
    file = request.FILES.get("pic")

    if not file:
        return HttpResponse("<h2>请先选择图片</h2>")

    print("type of file="+str(type(file)))
    # 构造存储路径
    fpath = '%s/booktest/%s' % (settings.MEDIA_ROOT, file.name)
    print("fpath="+fpath)
    # 读写保存
    with open(fpath,'wb') as pic:
        for c in file.chunks():
            pic.write(c)
    # 上传成功将文件路径保存进数据库
    UploadPic.objects.create(path="booktest/%s"%file.name)

    return redirect("/pics")


def show_pics(request):
    pics = UploadPic.objects.all()
    print("pics=" + str(pics))
    return render(request, 'booktest/show_pics.html', {"pics": pics})


# ---------------------下面是--分页--测试部分------------------'''
def show_provinces(request):
    # 1.查询出所有省级地区的信息
    areas = models.AreaInfo.objects.filter(aparent_id__isnull=True)
    # 2.获取index参数
    index = 1
    if request.method == "GET":
        index = request.GET.get("index", 1)
    elif request.method == "POST":
        index = request.POST.get("index", 1)

    paginator = Paginator(areas, 10)
    page = paginator.page(index)

    # 2.渲染模板
    return render(request, 'booktest/show_provinces.html', {"page": page})


def show_areas(request):
    return render(request, 'booktest/show_areas.html', {})


def get_areas(request):
    if request.method == "GET":
        area_id = request.GET.get("areaid")
    elif request.method == "POST":
        area_id = request.POST.get("areaid")

    if area_id : # 如果有值，说明用户传了，则查找对应id的下级地区
        onearea = models.AreaInfo.objects.get(id=area_id)
        areas = onearea.areainfo_set.all()
    else: # 如果没值，则获取所有省级地区返回
        areas = models.AreaInfo.objects.filter(aparent_id__isnull=True)

    response_list = []
    if areas.count()>0:
        for area in areas:
            response_list.append((area.id, area.atitle))

    return JsonResponse({"data": response_list})