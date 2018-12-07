price=input("请输入苹果单价：\n")
weight=input("请输入购买重量：\n")

money=float(price)*float(weight)
print("苹果单价 %.2f 元/斤，购买了 %.3f 斤，需要支付 %.4f 元" %(float(price),float(weight),money))