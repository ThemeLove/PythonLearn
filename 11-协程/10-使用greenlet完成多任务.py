import time
from greenlet import greenlet

"""
多个greenlet之间可以利用switch方法随意切换
"""


def task_one():
    while True:
        print("-------task one--------")
        green_two.switch()  # 切换到green_two执行
        time.sleep(0.5)


def task_two():
    while True:
        print("-------task two--------")
        green_one.switch()  # 切换到green_two执行
        time.sleep(0.5)


green_one = greenlet(task_one) # 创建green_onw
green_two = greenlet(task_two) # 创建green_two
green_one.switch() # 切换到green_one中执行

#
# def main():
#     global green_one
#     global green_two
#     green_one = greenlet(task_one(10))
#     green_two = greenlet(task_two(10))
#
#
#
#
# if __name__ == "__main__":
#     main()
