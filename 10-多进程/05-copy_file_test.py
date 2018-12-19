import os
from common import file_utils


def main():
    source_path = input("请输入文件目录：")
    files_count = file_utils.count_dir_num(source_path)
    print(source_path+"一共有 " + str(files_count) + " 个文件")
    file_utils.copy_dir(source_path,source_path+"_temp")


if __name__ == "__main__":
    main()
