import threading
import time


def sing(num):
    for i in range(num):
        print("我正在唱歌中.....")
        time.sleep(1)


def dance(num):
    for i in range(num):
        print("我正在跳舞中.....")
        time.sleep(1)


'''
python中threading.Thread方法可以创建一个线程
'''


def main():
    thread1 = threading.Thread(target=sing, args=(1000,))
    thread2 = threading.Thread(target=dance, args=(1000,))

    thread1.start()

    thread2.start()


if __name__ == "__main__":
    main()
