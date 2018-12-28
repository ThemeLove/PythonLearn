import multiprocessing
import os
import logging


def count_dir_num(source_path):
    """
    计算一个目录下及其子目录下所有文件的数量
    :param source_path: 目标目录
    :return: 文件数量
    """
    total_count = 0
    if os.path.isdir(source_path):
        files = os.listdir(source_path)
        for file in files:
            if os.path.isdir(source_path + "/"+file):
                total_count += count_dir_num(source_path + "/"+file)
            else:
                total_count += 1

    else:
        total_count += 1
    return total_count


def copy_file(queue, source_file, target_file):
    """
    copy文件
    :param queue :进程间队列
    :param source_file:源文件
    :param target_file:目标文件
    :return:
    """
    # global queue
    rf = open(source_file, "rb")
    read_data = rf.read()
    rf.close()

    wf = open(target_file, "wb")
    wf.write(read_data)
    wf.close()

    # print(source_file+"拷贝完成!")
    queue.put(source_file)


def copy_dir(pool, queue, source_path, target_path):
    """
    copy文件或文件夹
    :param pool:  进程池
    :param queue :进程间队列
    :param source_path:源目录
    :param target_path:目标目录
    :return:
    """
    try:
        # 如果目标目录不存在，则创建
        if os.path.exists(target_path):
            pass
        else:
            os.mkdir(target_path)

        if os.path.isdir(source_path):
            files = os.listdir(source_path)
            for file in files:
                if os.path.isdir(source_path + "/" + file):
                    copy_dir(pool, queue, source_path + "/" + file, target_path + "/" + file)
                else:
                    # print("source_file= "+source_path+"/"+file)
                    # print("target_file= "+target_path+"/"+file)
                    # print("开始拷贝"+file+"----->"+target_path+"/"+file)
                    pool.apply_async(copy_file, args=(queue, source_path + "/" + file, target_path + "/" + file))
        else:
            pool.apply_async(copy_file, args=(queue, source_path, target_path))
    except IOError as e:
        logging.exception(e)


def main():
    # 1.输入要拷贝的目录
    source_path = input("请输入要拷贝的文件目录：\n")
    # 2.生成目标文件夹目录
    target_path = ""
    try:
        target_path = source_path + "_temp"
        os.mkdir(target_path)
    except IOError as e:
        logging.exception(e)

    # 3.定义全局变量进程池
    pool = multiprocessing.Pool(3)
    # 4.定义全局变量进程间队列
    queue = multiprocessing.Manager().Queue()

    print(pool)
    print(queue)

    # file_names = os.listdir(source_path)
    # print("file_name= " + str(file_names))

    #     计算要拷贝的总个数
    total_num = count_dir_num(source_path)
    print("total_count= " + str(total_num))
    has_copy_count = 0

    # 5.开始拷贝
    copy_dir(pool, queue, source_path, target_path)

    # 6.关闭进程池
    pool.close()

    # pool.join()

    while True:
        file_name = queue.get() # queue.get()会阻塞，如果没有获取到值，后面的代码都不执行
        has_copy_count += 1
        # print("has_copy_count=" + str(has_copy_count))
#       打印拷贝的进度
        print("\r拷贝的进度%.2f %%" % (has_copy_count*100/total_num), end="")
#       退出循环的条件
        if has_copy_count >= total_num:
            # print("break")
            break
    print()


if __name__ == "__main__":
    main()
