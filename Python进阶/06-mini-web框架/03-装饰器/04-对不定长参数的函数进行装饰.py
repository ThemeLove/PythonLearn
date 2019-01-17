def set_func(func):
    print("-----开始进行装饰")

    def call_func(*args, **kwargs):
        print("-----权限验证1-----")
        print("-----权限验证2-----")
        # 特别注意这里给原函数传参数时一定要用*args和**kwargs,因为*args和**kwargs会对参数进行自动拆包
        # *args 对元祖拆包，**kwargs对字典进行拆包
        func(*args, **kwargs)

        #  args不会自动拆包，会把所有的可变参数都放在一个元祖里
        #  kwargs不会自动拆包，会把所有的关键字参数都放到一个字典里
        # func(args, kwargs)
    return call_func


@set_func
def test1(num, *args, **kwargs):
    print("-----test1-----%d" % num)


test1(100)
test1(200, 100)
test1(300, 100, kw=100)


