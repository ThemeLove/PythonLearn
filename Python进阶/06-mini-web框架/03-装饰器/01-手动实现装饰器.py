#   decorator 的作用就是在不改动原方法的前提下对原方法的功能进行装饰
def decorator(func):
    print("-----开始装饰-----")

    #  定义一个方法装饰方法,其实是一个闭包,在闭包中调用原方法
    def call_func():
        print("-----装饰器添加的功能-----")
        func()
    return call_func  # 返回方法的引用


#  test为测试方法，待装饰的方法
def test():
    print("-----test-----")


#  装饰器的手动实现其实就是：将原方法的引用test传入到decorator中，用test重新接收decorator中返回的新方法，
#  相当于将test的指向由原方法改为装饰器中返回的新方法
#  这样再调用test()的时候就是调用新方法，即可以先执行新方法中添加的功能，再在新方法中调用原方法
#  这样就做到了在不修改原方法的前提下修改了功能，这对已经上线很久的功能进行修改很有效
test = decorator(test)
test()
