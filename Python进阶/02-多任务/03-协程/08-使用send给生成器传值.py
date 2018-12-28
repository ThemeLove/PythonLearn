import logging

def generator(num):
    count = 0
    while count <= num:
        send_ret = yield count # 当使用生成器对象调用send方法传值时，就相当于给yield count 该行赋值
        print("send_ret=", send_ret)
        if isinstance(send_ret, int):
            count += send_ret
        else:
            count += 1


"""
next 和 send 方式获取生成器的值的区别 
1.当使用next取值时，生成器会接着上次yield暂停的地方继续向下执行，直到再次执行到yield的时候会把yield后面的值返回，如果执行不到就会报StopIteration的异常
2.如果是第一次获取值时send只能传None，否则会报错；如果不是第一次就会把传的值赋值给yield行（yield 和yield后面的表达式一起），在程序中可以用变量接收并使用。
"""


def main():
    gen10 = generator(10)

    print("first get = ",next(gen10))
    try:
        while True:
            print(gen10.send(2))
    except StopIteration as e:
        logging.exception(e)

    # print(gen5.send(4)) # 报错，send在生成器第一次调用的时候不能传non-None值
    # print(next(gen5))
    # print(gen5.send(None)) # 不报错，因为传的值为None
    # print(gen5.send(4))


if __name__ == "__main__":
    main()
