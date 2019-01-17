class Test:
    def __init__(self, func):
        self.func = func

    def __call__(self, num):
        print("Test----->开始装饰")
        print("add_10----->num=%d" % self.func(num))


@Test  # 等同于add_10 = Test(add_10)， Test(add_10)时会去调用__call__方法
def add_10(num):
    return num + 10


num1 = add_10(100)
