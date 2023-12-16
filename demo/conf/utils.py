import os
import shutil

def createdFile(name):
    '创建文件夹'
    if not os.path.exists(name):
        os.makedirs(name)


def getFileList(name):
    '返回文件夹所有文件'
    file_ls = os.listdir(name)  # 获取所有文件名称
    return file_ls


def delFile(path):
    '删除文件夹下所有文件'
    if not os.listdir(path):
        print('目录为空！')
    else:
        for i in os.listdir(path):
            path_file = os.path.join(path, i)  # 取文件绝对路径
            if os.path.isfile(path_file):
                os.remove(path_file)
            else:
                delFile(path_file)
                shutil.rmtree(path_file)