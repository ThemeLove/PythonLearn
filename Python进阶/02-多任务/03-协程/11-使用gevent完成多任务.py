import gevent
from gevent import monkey
import time

# monkey.patch_all() 会自动打补丁，一般为阻塞方法
monkey.patch_all()


def task_one(num):
    for i in range(num):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


def task_two(num):
    for i in range(num):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


def task_three(num):
    for i in range(num):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


g1 = gevent.spawn(task_one, 5)
g2 = gevent.spawn(task_two, 5)
g3 = gevent.spawn(task_three, 5)
g1.join()
g2.join()
g3.join()
