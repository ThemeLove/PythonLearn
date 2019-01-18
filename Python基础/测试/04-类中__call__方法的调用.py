class Person:
    def __init__(self, name):
        self.name = name

    def __call__(self, msg):
        print("__call__")
        print(msg + " " + self.name)


# 创建一个name为laoli的Persion对象
per1 = Person("laoli")

# 当用  对象（param）时，会去调用对象中的__call__方法，并且可以传参
# 当用per1()时会去调用per1对象中的__call__方法
per1("hello")
