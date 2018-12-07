price_str=input("请输入苹果的单价：\n")
weight_str=input("请输入苹果的重量：\n")

# 转化为float类型
price=float(price_str)
weight=float(weight_str)

# 计算总价
money=price * weight
print("苹果的总价为："+str(money)+"元")
