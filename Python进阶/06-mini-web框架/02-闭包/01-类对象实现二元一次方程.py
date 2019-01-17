'''
本例实现y=kx+b的二元一次方程
1.因为类对象会自带各种魔法放，成员属性，所以占用空间较多
'''


class GetY:
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def getY(self, x):
        return self.k*x+self.b


line1 = GetY(1, 1)  # 创建一条线line1
print("line1_y1=", line1.getY(0))
print("line1_y2=", line1.getY(1))
print("line1_y3=", line1.getY(2))

print("---"*20)
line2 = GetY(2, 2)  # 创建一条线line2
print("line2_y1=", line2.getY(0))
print("line2_y2=", line2.getY(1))
print("line2_y3=", line2.getY(2))
