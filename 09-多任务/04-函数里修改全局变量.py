test_num = 10
test_str = "hello"
test_list = [10, 20]
test_tuple = (1, 2)


'''
在Python的函数中修改全局变量时:
1.只要是修改变量前后所应应的内存地址值没有变化，就不需要加global修饰
2.只要是修改变量前后所对应的内存地址址有变化就需要添加global修饰，
因为一般不可变对象比如int、字符串、元祖在作运算时地址值都会变化，所以需要加global
3.Python中可以用id()函数来查看一个变量的内存地址值
'''


def change_num():
    global test_num
    test_num += 10
    print("change_num= "+str(test_num))


def change_str():
    global test_str
    test_str += " python"
    print(test_str)


def change_list():
    # test_list.append(30)
    global test_list
    test_list += [30, 40]
    print("change_list= "+str(test_list))


def change_tuple():
    global test_tuple
    test_tuple = (1, 2)
    print(id(test_tuple))


def main():
    print("before change_num= "+str(test_num))
    change_num()

    print("before change_str= " + test_str)
    change_str()

    print("before change_list= "+str(test_list))
    change_list()

    print("before change_tuple id= "+str(id(test_tuple)))
    change_tuple()


if __name__ == "__main__":
    main()
