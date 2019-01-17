def set_func(func):
    print("-----开始进行装饰")

    def call_func(*args, **kwargs):
        print("-----权限验证1-----")
        print("-----权限验证2-----")
        #  如果要装饰的原函数有返回值，这里也要同步return，才可以在外部接收返回值
        return func(*args, **kwargs)
    return call_func


@set_func
def test1(num, *args, **kwargs):
    print("-----test1-----%d" % num)
    return num


@set_func
def test2():
    pass


num1 = test1(100)
print("num1=", num1)
num2 = test1(200, 100)
print("num2=", num2)
num3 = test1(300, 100, kw=100)
print("num3=", num3)


ret2 = test2()
print("ret2", ret2)


