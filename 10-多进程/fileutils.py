import os


def copy_dir(source_path, target_path):
    """
    copy文件或文件夹
    :param source_path:源目录
    :param target_path:目标目录
    :return:
    """
    if os.path.isdir(source_path):
        files = os.listdir(source_path)
        for file in files:
            if os.path.isdir(file):
                copy_dir(file, target_path + "/" + file)
            else:
                copy_file(file, target_path + "/" + file)
    else:
        copy_file(source_path, target_path)


def copy_file(source_file, target_file):
    """
    copy文件
    :param source_file:源文件
    :param target_file:目标文件
    :return:
    """
    with open(target_file, "wb") as wf:
        with open(source_file,"rb") as rf:
            while True:
                read_data=rf.read(1024)
                print(type(read_data))
                if not read_data:
                    break
                wf.write(read_data)
