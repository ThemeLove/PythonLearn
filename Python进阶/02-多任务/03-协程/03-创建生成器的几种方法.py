def fibonacci(num):
    """
    生成器实现Fibonacci
    :param num:表示生成的fibonacci的元素个数
    :return:
    """
    count = 0
    a, b = 0, 1
    while count < num:
        yield a
        a, b = b, a + b
        count += 1


def main():
    #  1.将列表生成式的[] 变成（）即可创建一个生成器对象
    list1 = [m + str(n) for m in "abc" for n in range(7) if n % 2 == 0]
    generator1 = (m + str(n) for m in "abc" for n in range(7) if n % 2 == 0)
    print("list1= ", list1)
    print("generator1= ", generator1)
    print("list1 type= ", type(list1))
    print("generator1 type= ", type(generator1))

    for temp in generator1:
        print(temp)

    print("----------------------\n\n\n\n\n\n")

    #  2.用yield在函数中来定义生成器，只要函数中有yield，就称为生成器
    fib0 = fibonacci(0)
    fib1 = fibonacci(1)
    fib2 = fibonacci(2)
    fib3 = fibonacci(3)
    fib10 = fibonacci(10)

    print("fib0 type= ", type(fib0))
    print("fib1 type= ", type(fib1))
    print("fib2 type= ", type(fib2))
    print("fib3 type= ", type(fib3))
    print("fib10 type= ", type(fib10))

    # print("fib0 next= ", next(fib0)) 特别说明，这里如果直接调用，会抛出一个StopIteration的异常；
    # 但是下面的for.. in 却不会报这个异常，说明for..in中默认捕获了这个异常
    for temp in fib0:
        print("fib0---->", temp)
    print("----------------------\n")

    # print("fib1 next= ", next(fib1))
    for temp in fib1:
        print("fib1---->", temp)
    print("----------------------\n")

    for temp in fib2:
        print("fib2---->", temp)
    print("----------------------\n")

    for temp in fib3:
        print("fib3---->", temp)
    print("----------------------\n")

    # print("fib10 next= ", next(fib10))
    for temp in fib10:
        print("fib10---->", temp)
    print("----------------------\n")


if __name__ == "__main__":
    main()
