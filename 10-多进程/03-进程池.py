import multiprocessing
import time, os, random


def worker(msg):
    time_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random()*2)
    time_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (time_stop-time_start))


'''
    1.pool.close()调用后不能在pool中添加进程
    2.当使用进程池时必须调用pool.join()方法，让主进程等待所有子进程执行完毕，再继续执行主进程的代码；
    否则主进程的代码不阻塞，立即执行，执行完毕后主进程结束，程序结束，所有子进程也不复存在
'''


def main():
    # 创建一个进程池，最大进程数为3
    pool = multiprocessing.Pool(3)
    for i in range(0, 10):
        # Pool.apply_async(要调用的目标，（传递给目标的参数元祖，）)
        # 每次循环讲会用空闲出来的子进程去调用目标
        pool.apply_async(worker, (i,))
    print("-----start-----")
    # 关闭进程池，关闭后pool不再接收新的请求
    pool.close()
    # 等待pool中的所有子进程执行完成，必须放在close语句之后
    pool.join()
    print("-----end-----")


if __name__ == "__main__":
    main()
