import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()
test_num = 0


def test1(num):

    print("-----线程： "+str(threading.current_thread().getName())+" 进来了")
    global test_num

    lock_a.acquire()
    print("-----lock_a 锁住了-----")
    print("-----线程： " + str(threading.current_thread().getName()) + " sleep 2 秒钟")
    time.sleep(2)

    for i in range(num):
        print("-----线程： " + str(threading.current_thread().getName()) + " 醒了，继续执行")
        print("-----等待 lock_b 的锁")
        lock_b.acquire()
        test_num += 1
        lock_b.release()

        print("-----test1-----")

    lock_a.release()


def test2(num):
    print("-----线程： " + str(threading.current_thread().getName()) + " 进来了")
    global test_num

    lock_b.acquire()
    print("-----lock_b 锁住了-----")

    for i in range(num):
        print("-----等待 lock_a 的锁")
        lock_a.acquire()
        test_num += 1
        lock_a.release()

        print("-----test2-----")

    lock_b.release()


'''
1.threading.Lock()能够解决全局中多线程共同操作全局变量线程安全的问题，但是多个同步锁存在时也可能造成死锁问题。
2.死锁的根本原因是不同的锁都等待对方先释放才能继续执行，导致程序无休止等待的现象
3.变成中应尽量避免
'''


def main():
    thread1 = threading.Thread(target=test1, args=(1000,))
    thread2 = threading.Thread(target=test2, args=(1000,))

    thread1.start()

    time.sleep(1)

    thread2.start()


if __name__ == "__main__":
    main()
