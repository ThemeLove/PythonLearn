import multiprocessing
import os
import logging

# 定义全局变量进程池
pool = multiprocessing.Pool(3)
# 定义全局变量进程间队列
queue = multiprocessing.Manager().Queue()


def copy_file(source_file, target_file):
    """
    copy文件
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

    print(source_file+"拷贝完成!")
    queue.put(source_file)


def copy_dir(source_path, target_path):
    """
    copy文件或文件夹
    :param source_path:源目录
    :param target_path:目标目录
    :return:
    """
    # global pool
    if os.path.isdir(source_path):
        files = os.listdir(source_path)
        for file in files:
            if os.path.isdir(file):
                copy_dir(source_path+"/"+file, target_path + "/" + file)
            else:
                # print("source_file= "+source_path+"/"+file)
                # print("target_file= "+target_path+"/"+file)
                # print("开始拷贝"+file+"----->"+target_path+"/"+file)
                pool.apply_async(copy_file, args=(source_path+"/"+file, target_path + "/" + file))
    else:
        pool.apply_async(copy_file, args=(source_path, target_path))


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

    print(pool)
    print(queue)

    file_names = os.listdir(source_path)
    print("file_name= " + str(file_names))

    # 5.开始拷贝
    copy_dir(source_path, target_path)

    # 6.关闭进程池
    pool.close()

    # pool.join()

#     计算要拷贝的总个数
    total_num = len(file_names)
    print("total_count= " + str(total_num))
    has_copy_count = 0
    while True:
        file_name = queue.get()
        has_copy_count += 1
        print("has_copy_count="+ str(has_copy_count))
#       打印拷贝的进度
        print("\r拷贝的进度%.2f %%" % (has_copy_count*100/total_num), end="")
#       退出循环的条件
        if has_copy_count >= total_num:
            print("break")
            break
    print()


if __name__ == "__main__":
    main()
