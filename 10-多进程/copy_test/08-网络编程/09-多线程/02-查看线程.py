import threading
import time


def test1(num):
    print("----test111111 start-----")
    for i in range(num):
        print("-----test1-----%d" % i)
        time.sleep(1)
    print("-----test1111111 end-----")


def test2(num):
    print("-----test222222 start-----")
    for i in range(num):
        print("-----test2-----%d" % i)
        time.sleep(1)
    print("-----test222222 end-----")


'''
threading.enumerate()  返回一个包含正在运行的线程的list
threading.current_thread().getName() 可以查看当前代码运行的线程名
python中主线程等待所有子线程执行完毕，主线程才能结束
type()函数能够查看一个对象的类型
'''


def main():

    thread1 = threading.Thread(target=test1, args=(5,))
    thread2 = threading.Thread(target=test2, args=(5,))

    print(type(threading.enumerate()))

    print(threading.enumerate())

    thread1.start()
    print(threading.enumerate())

    time.sleep(3)
    thread2.start()
    print(threading.enumerate())

    time.sleep(3)
    print(threading.enumerate())

    time.sleep(4)
    print(threading.enumerate())


if __name__ == "__main__":
    main()
