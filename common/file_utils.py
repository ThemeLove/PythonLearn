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


def copy_dir(source_path, target_path):
    """
    copy文件或文件夹
    :param source_path:源目录
    :param target_path:目标目录
    :return:
    """
    try:
        # 如果目标目录不存在，则先创建
        if os.path.exists(target_path):
            pass
        else:
            os.mkdir(target_path)

        if os.path.isdir(source_path):
            files = os.listdir(source_path)
            for file in files:
                if os.path.isdir(source_path + "/" + file):
                    copy_dir(source_path + "/" + file, target_path + "/" + file)
                else:
                    copy_file(source_path + "/" + file, target_path + "/" + file)
        else:
            copy_file(source_path, target_path)
    except IOError as e:
        logging.exception(e)


def copy_file(source_file, target_file):
    """
    copy文件
    :param source_file:源文件
    :param target_file:目标文件
    :return:
    """
    with open(target_file, "wb") as wf:
        with open(source_file, "rb") as rf:
            while True:
                read_data = rf.read(1024)
                # print(type(read_data))
                if not read_data:
                    break
                wf.write(read_data)
