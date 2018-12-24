import time
import logging


"""
简单版的协程完成多任务
1.利用yield保存和恢复cpu的特性 
2.自己实现管理和切换协程的功能
"""


def task_one(num):
    count = 0
    while count <= num:
        print("-------task one--------")
        time.sleep(0.5)
        yield   # 利用yield保存和恢复cpu的特性
        count += 1


def task_two(num):
    count = 0
    while count <= num:
        print("-------task two--------")
        time.sleep(0.5)
        yield
        count += 1


def main():
    one10 = task_one(10)
    two10 = task_two(10)
    # 自己实现管理和切换协程的功能
    try:
        while True:
            next(one10)
            next(two10)
    except StopIteration as e:
        logging.exception(e)


if __name__ == "__main__":
    main()
