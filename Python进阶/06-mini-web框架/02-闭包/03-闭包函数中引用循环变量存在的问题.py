def loop_test():
    fs = []
    for i in range(3):

        def call_func():
            print("i=", i)
        fs.append(call_func)
    return fs



'''
从打印结果可以看出闭包是调用的时候才执行，因为在执行时i的值已经是2，所以3个打印都是2，而不是0、 1、 2
在使用的时候应该避免出现这种情况，容易已发bug
总结：返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
'''
fs = loop_test()
fs[0]()  # i= 2
fs[1]()  # i= 2
fs[2]()  # i= 2
