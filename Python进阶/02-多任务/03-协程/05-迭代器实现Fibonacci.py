from collections import Iterator


class Fibonacci:
    def __init__(self, num):
        self.count = 0
        self.a = 0
        self.b = 1
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return ret
        else:
            raise StopIteration()


def main():
    fib0 = Fibonacci(0)
    fib1 = Fibonacci(1)
    fib2 = Fibonacci(2)
    fib3 = Fibonacci(3)
    fib10 = Fibonacci(10)

    print("type fib0= ", type(fib0))
    print("type fib1= ", type(fib1))
    print("type fib2= ", type(fib2))
    print("type fib3= ", type(fib3))
    print("type fib10= ", type(fib10))

    print("fib0= ", fib0)

    print("fib0 is Iterator= ", isinstance(fib0,Iterator))

    for temp in fib0:
        print("fib0----->", temp)
    print("-----------------\n\n\n")

    for temp in fib1:
        print("fib1----->", temp)
    print("-----------------\n\n\n")

    for temp in fib2:
        print("fib2----->", temp)
    print("-----------------\n\n\n")

    for temp in fib3:
        print("fib3----->", temp)
    print("-----------------\n\n\n")

    for temp in fib10:
        print("fib10----->", temp)


if __name__ == "__main__":
    main()