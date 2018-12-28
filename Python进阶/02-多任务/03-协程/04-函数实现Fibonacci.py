
def fibonacci(num):
    """
    利用函数实现斐波拉契数列，这里的一个弊端就是会生成一个list返回，里面保存了全部的斐波拉契元素；
    如果入参num比较大，那么占用内存就会很大
    :param num: 入参，生成斐波拉契的元素个数
    :return: 返回一个斐波拉契数列
    """
    count = 0
    ret_list = list()
    a, b = 0, 1
    while True:
        if count >= num:
            break
        else:
            ret_list.append(a)
            a, b = b, a+b
        count += 1

    return ret_list


def main():

    list0 = fibonacci(0)
    list1 = fibonacci(1)
    list2 = fibonacci(2)
    list3 = fibonacci(3)
    list10 = fibonacci(10)

    print("list0= ", list0)
    print("list1= ", list1)
    print("list2= ", list2)
    print("list3= ", list3)
    print("list10= ", list10)


if __name__ == "__main__":
    main()
