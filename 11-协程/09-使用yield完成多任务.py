import time
import logging


def task_one(num):
    count = 0
    while count <= num:
        print("-------task one--------")
        time.sleep(0.5)
        yield
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
    try:
        while True:
            next(one10)
            next(two10)
    except StopIteration as e:
        logging.exception(e)


if __name__ == "__main__":
    main()
