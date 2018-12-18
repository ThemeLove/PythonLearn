import multiprocessing
import os
import logging


def copy_file(queue, source_dir, target_folder, file_name):

    source_file_name = source_dir + "/" + file_name
    target_file_name = target_folder + "/" + file_name
    print("拷贝"+source_file_name+"----->"+target_file_name+"开始")

    f_old = open(source_file_name, "rb")
    file_content = f_old.read()
    f_old.close()

    print("file_content="+ file_content)
    f_new = open(target_file_name, "wb")
    f_new.write(file_content)
    f_new.close()

    print(str(source_file_name)+" 拷贝完成！")
#   读写完一个文件，要将该文件名放到queue中
    queue.put(source_file_name)


def main():

    # 1.创建进程池
    cpu_count = multiprocessing.cpu_count()
    print("cpu_count= "+str(cpu_count))
    pool = multiprocessing.Pool(3)
    # 2.创建进程间队列
    queue = multiprocessing.Manager().Queue()
    # 3.输入要拷贝的目录
    source_dir = input("请输入要拷贝的文件目录：\n")
    print("source_dir= "+source_dir)

    # 创建一个新的文件夹
    target_folder = ""
    try:
        target_folder = source_dir + "_temp"
        os.mkdir(target_folder)
        print("target_folder "+target_folder+"创建成功")
    except IOError as e:
        logging.exception(e)

    file_names = os.listdir(source_dir)
    print("file_name= " + str(file_names))

    for file_name in file_names:
        # 4.开启任务
        pool.apply_async(copy_file, args=(queue, source_dir, target_folder, file_name))

    # 5.关闭进程池
    pool.close()

    # pool.join()

#     计算要拷贝的总个数
    total_num = len(file_names)
    print("total_count= "+ str(total_num))
    has_copy_count = 0
    while True:
        file_name = queue.get()
        has_copy_count += 1
#       打印拷贝的进度
        print("\r拷贝的进度%.2f %%" % (has_copy_count*100/total_num))
#       退出循环的条件
        if has_copy_count >= total_num:
            break
    print()


if __name__ == "__main__":
    main()
