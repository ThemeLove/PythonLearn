def add_h1(func):
    print("add_h1----->开始装饰了")  # 注意这句代码在添加了装饰器的时候就执行了，而不是函数调用的时候

    def call_func(str):
        print("add_h1----->执行了")
        return "<h1>"+func(str)+"</h1>"
    return call_func


def add_h2(func):
    print("add_h2----->开始装饰了")

    def call_func(str):
        print("add_h2----->执行了")
        return "<h2>"+func(str)+"</h2>"
    return call_func


'''
多个装饰器装饰同一个函数时流程解释：
1.代码从上到下执行，当执行到@add_h1的时候，因为@add_h1下面是@add_h2,因为装饰器可以装饰函数，但是不能装饰@add_h2;
所以继续向下执行遇到@add_h2,而@add_h2下面是一个函数，所以可以正常装饰并且得到一个装饰后的函数； 
再回到@add_h1，这时@add_h1下面可以看成是进过@add_h2装饰的新函数，所以@add_h1在此基础上再次装饰；
最终得到的结果就是test_str是先进过add_h2装饰再经过add_h1装饰的新函数，
就相当新函数的内部包装了add_h1,add_h1内部包装了add_h2,所以执行的时候是先执行add_h1再执行add_h2,最后执行原函数
'''


@add_h1
@add_h2
def test_str(str):
    return "我是测试文字: %s" % str


str1 = test_str("hello")
print("str1=", str1)
# str2 = test_str("decorator")
# print("str2=", str2)
