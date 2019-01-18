def decorator_with_param(num):

    def decorator(func):

        def call_func(str):
            if num == 1:
                print("-----添加权限验证1-----")
            elif num == 2:
                print("-----添加权限验证2-----")
            else:
                print("-----添加其他权限验证-----")
            func(str)
        return call_func
    return decorator


@decorator_with_param(1)
def test(str):
    print("我是业务功能： " + str)


@decorator_with_param(2)
def test2(str):
    print("我是业务功能： " + str)


func1 = test("login")
# func1()

func2 = test2("pay")
# func2()
