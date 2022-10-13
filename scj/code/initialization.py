# 初始化相关功能的实现

import os
from configparser import ConfigParser


# 获取存储结构的根目录
def get_root_path():
    # 此处暂时定位到测试目录，后面需要修改
    root = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    return os.path.join(root, "dir_test")


# 初次安装软件时，创建存储环境
def directory_ini():
    path = get_root_path()
    if os.path.isdir(path + "/data") is not True:  # 初始化data文件夹
        os.mkdir(path + "/data")
    if os.path.isdir(path + "/data/device") is not True:  # 初始化device设备文件夹
        os.mkdir(path + "/data/device")
    if os.path.isfile(path + "/data/device_list.yml") is not True:  # 初始化配置文件
        print(path + "/data/device_list.yml")
        with open(path + "/data/device_list.yml", 'a') as f:
            f.close()
    if os.path.isdir(path + "/model") is not True:  # 初始化model文件夹
        os.mkdir(path + "/model")
    if os.path.isdir(path + "/model/data_set") is not True:  # 初始化model中的临时训练数据集文件夹
        os.mkdir(path + "/model/data_set")
    if os.path.isdir(path + "/model/models") is not True:  # 初始化存放模型的文件夹
        os.mkdir(path + "/model/models")
    if os.path.isfile(path + "/model/models/model_list.yml") is not True:  # 初始化配置文件
        with open(path + "/model/models/model_list.yml", 'a') as f:
            f.close()
    if os.path.isfile(path + "/system.ini") is not True:  # 初始化配置文件
        conf = ConfigParser()
        conf.read(path + "/system.ini")
        conf.add_section('path_config')
        conf.set('path_config', 'root_path', path)
        conf.set('path_config', 'device_path', path + "/data/device")
        conf.set('path_config', 'model_path', path + "/model/models")
        conf.set('path_config', 'data_set_path', path + "/model/data_set")
        conf.set('path_config', 'device_list_path', path + "/data/device_list.yml")
        conf.set('path_config', 'model_list_path', path + "/model/models/model_list.yml")
        conf.add_section('processing')
        conf.set('processing', 'video', "none")
        conf.set('processing', 'camera', "none")
        conf.set('processing', 'model', "none")
        with open(path + "/system.ini", 'a') as f:
            conf.write(f)
            f.close()


if __name__ == '__main__':
    print(get_root_path())
    directory_ini()