from collections import Iterable
from collections import Iterator


def generator(num):
    count = 0
    while count < num:
        yield count
        count += 1
    return "i'm the result of generator"


'''
1.经测试只有第一次捕获到StopIteration异常的时候，才能通过e.value获取到生成器的值
2.for..in中默认捕获了异常

'''


def main():
    gen2 = generator(2)
    gen10 = generator(10)
    # for temp in gen10:
    #     print("gen10----->", temp)

    print(isinstance(gen2, Iterable))
    print(isinstance(gen2, Iterator))
    try:
        print(next(gen2))
        print(next(gen2))
        # print(next(gen2))
    except StopIteration as e:
        print("e.value= %s" % e.value)

    try:
        print(next(gen2))
        print(next(gen2))
        print(next(gen2))
    except StopIteration as e:
        print("e.value= %s" % e.value)

    # 再获取一次就会有异常产生，这里手动捕获
    try:
        while True:
            temp = next(gen10)
            print("gen10----->", temp )
    except StopIteration as e:
        print("e.value= %s" % e.value)

    try:
        next(gen10)
    except StopIteration as e:
        print("e.value= %s" % e.value)

    next(gen10)


if __name__ == "__main__":
    main()
