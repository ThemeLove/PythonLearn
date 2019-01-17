'''
一个函数返回一个定义在该函数内部的函数的引用，而内部函数通常又引用该函数中的局部变量，通常这样的函数就叫着闭包

另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到被调用才执行
'''


'''本例实现y=kx+b的二元一次方程
用闭包的好处：
1.即保存了完成功能的函数代码
2.又隔离了用到的局部变量
3.比用类对象的实现方式占用更小的空间
4.较为简单的逻辑功能可以替代类来实现，如果较为复杂还是建议用类来实现
'''
def get_y(k, b):
    def call_func(x):
        y = k*x+b
        return y
    return call_func


line1 = get_y(1, 1)
print("line1_y1=", line1(0))
print("line1_y2=", line1(1))
print("line1_y3=", line1(2))

print("---"*20)
line2 = get_y(2, 2)
print("line2_y1=", line2(0))
print("line2_y2=", line2(1))
print("line2_y3=", line2(2))

line3 = get_y(2, 2)
print(line2 == line3)  # False 表示虽然参数相同，但是指向了不同的内存地址，类似于2个初始化相同的对象
