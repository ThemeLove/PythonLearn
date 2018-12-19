class Ship:
    def __init__(self, name, price ,speed):
        self.name = name
        self.price = price
        self.speed = speed

    def msg(self):
        print("name=%s,price=%d,speed=%d" %(self.name,self.price,self.speed))
