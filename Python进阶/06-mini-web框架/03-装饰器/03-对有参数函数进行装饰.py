#   decorator 的作用就是在不改动原方法的前提下对原方法的功能进行装饰
def decorator(func):
    print("-----开始装饰-----")

    #  和原方法参数一样定义一个形式参数
    def call_func(num):
        print("-----装饰器添加的功能-----")
        func(num)  # 把形式参数同步传入到func里
    return call_func  # 返回方法的引用


#  python中装饰器的实现：在被装饰的方法上添加@decorator
#  @decorator的作用就相当于手动实现时test = decorator(test)
@decorator
def test(num):
    print("-----test-----%d" % num)


# 直接调用,传入参数
test(10)
