import threading

test_num = 0


def test1(num):
    global test_num
    for i in range(num):
        test_num += 1
    print("-----test1-----test_num= %d" % test_num)


def test2(num):
    global test_num
    for i in range(num):
        test_num += 1
    print("-----test2-----test_num= %d" % test_num)


'''
本例子中当传参数较大是，2个线程同时执行时，最终test_num的值不等于2000000，说明共享全局变量会存在资源竞争的问题，
导致程序的运行结果不是我们预期的那样。
根本原因是 test_num+=1 不是原子操作
    
'''


def main():
    thread1 = threading.Thread(target=test1, args=(1000000,))
    thread2 = threading.Thread(target=test2, args=(1000000,))

    thread1.start()

    thread2.start()


if __name__ == "__main__":
    main()
