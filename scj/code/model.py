import json
import os
import time
from configparser import ConfigParser
from scj.code import initialization
import yaml


# 选择使用某个模型
def set_model(index):
    """
    :param index: 模型的index
    :return:json = {
                "code": 1,  # 0
                "message": "ok"  # "error"
            }
    """
    res_dict = {
        "code": 0,
        "message": "error"
    }
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    model_list_path = conf["path_config"]["model_list_path"]
    with open(model_list_path, 'r') as f:  # 读取image list的内容
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    for model in yml_dict["model_list"]:
        if model["index"] == index:
            conf.set('processing', 'model', model["model_name"])
            with open(initialization.get_root_path() + "/system.ini", 'w') as f:
                conf.write(f)
                f.close()
            res_dict = {
                "code": 1,
                "message": "ok"
            }
            return json.dumps(res_dict, ensure_ascii=False)
    return json.dumps(res_dict, ensure_ascii=False)


# 获取模型列表
def get_model_list():
    """
    :return:
    json ={
        "model_list": [
        {"create_time": "20221207-18_06_59", "index": 2, "model_name": "2_model_20221207-18_06_59"},
        {"create_time": "20221207-18_07_11", "index": 3, "model_name": "3_model_20221207-18_07_11"},
        {"create_time": "20221207-18_07_14", "index": 4, "model_name": "4_model_20221207-18_07_14"}
        ],
        "model_num": 4
    }
    """
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    model_list_path = conf["path_config"]["model_list_path"]
    with open(model_list_path, 'r') as f:
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    return json.dumps(yml_dict, ensure_ascii=False)


# 删除某个模型
def delete_model(index):
    """
    :param index:要删除的模型idx
    :return: json = {
                "code": 1,  # 0
                "message": "ok"  # "error"
            }
    """
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    model_list_path = conf["path_config"]["model_list_path"]
    store_path = conf["path_config"]["model_path"]
    with open(model_list_path, 'r') as f:  # 读取image list的内容
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    res_dict = {
        "code": -1,
        "message": "index error"
    }
    for model in yml_dict["model_list"]:
        if model["index"] == index:
            for file in os.listdir(store_path + "/" + model["model_name"]):
                os.remove(store_path + "/" + model["model_name"] + "/" + file)
            os.removedirs(store_path + "/" + model["model_name"])
            yml_dict["model_list"].remove(model)
            with open(model_list_path, 'w+') as f:  # 修改image list
                yaml.dump(yml_dict, f, allow_unicode=True)
                f.close()
            res_dict = {
                "code": 1,
                "message": "ok"
            }
            return json.dumps(res_dict, ensure_ascii=False)
    return json.dumps(res_dict, ensure_ascii=False)


# 训练新模型
def train(parameter, dataset_path, old_model_idx=0, model_name=""):
    """
    :param dataset_path: 训练数据集地址
    :param parameter: 训练的模型参数
    :param old_model_idx: 在哪个模型基础上训练，默认不在旧的模型基础上训练
    :param model_name: 新模型的名字，不传入则默认起名
    :return:
    """
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    model_list_path = conf["path_config"]["model_list_path"]
    model_path = conf["path_config"]["model_path"]
    with open(model_list_path, 'r') as f:  # 读取image list的内容
        model_list_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    model_list_dict["model_num"] += 1
    time_str = time.strftime("%Y%m%d-%H_%M_%S", time.localtime())
    model_name = str(model_list_dict["model_num"]) + "_model_" + time_str if model_name == "" else model_name
    model_save_path = model_path + "/" + model_name
    os.mkdir(model_save_path)
    model_info = {
        "model_name": model_name,
        "index": model_list_dict["model_num"],
        "create_time": time_str
    }
    model_list_dict["model_list"].append(model_info)
    old_model_path = ""
    if old_model_idx != 0:
        for model in model_list_dict["model_list"]:
            if model["index"] == old_model_idx:
                old_model_path = model_path + "/" + model["name"]
                break
    with open(model_list_path, 'w+') as f:
        yaml.dump(model_list_dict, f, allow_unicode=True)
        f.close()
    return test_train(parameter=parameter, save_path=model_save_path, old_model_path=old_model_path, dataset_path=dataset_path)


# 模拟训练函数
def test_train(parameter, save_path, old_model_path, dataset_path):
    """
    :param parameter: 参数json
    :param save_path: 模型保存的位置(文件夹)
    :param old_model_path: 在哪个模型的基础上训练，该模型的地址，若为""则从头训练
    :return:
    """
    return


# 创建临时文件夹及临时文件
def mk_temp_dir(epoch):
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    model_path = conf["path_config"]["root_path"] + "/model/temp"
    if os.path.isdir(model_path) is not True:
        os.mkdir(model_path)
    if os.path.isfile(model_path + "/temp.yml") is not True:  # 初始化配置文件
        with open(model_path + "/temp.yml", 'a') as f:
            yaml_dict = {
                'total_epoch': epoch,
                'done_epoch': 0
            }
            yaml.dump(yaml_dict, f, allow_unicode=True)
            f.close()


# 删除临时文件夹及临时文件
def del_temp_dir():
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    model_path = conf["path_config"]["root_path"] + "/model/temp"
    for l in os.listdir(model_path):
        os.remove(model_path + "/" + l)
    os.removedirs(model_path)


# 更新训练的epoch, 调用一次+1
def set_tmp_epoch():
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    tmp_path = conf["path_config"]["root_path"] + "/model/temp/temp.yml"
    with open(tmp_path, 'r') as f:
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    yml_dict["done_epoch"] += 1
    with open(tmp_path, 'w+') as f:
        yaml.dump(yml_dict, f, allow_unicode=True)
        f.close()


# 获取当前训练的进度
def get_tmp_epoch():
    """
    :return: json = {"done_epoch": 3, "total_epoch": 10}
    """
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    tmp_path = conf["path_config"]["root_path"] + "/model/temp/temp.yml"
    with open(tmp_path, 'r') as f:
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    return json.dumps(yml_dict, ensure_ascii=False)


# 获取临时存储文件夹的路径
def get_tmp_dir_path():
    """
    :return: string 临时'文件夹'路径
    """
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    tmp_path = conf["path_config"]["root_path"] + "/model/temp/"
    return tmp_path


if __name__ == '__main__':
    # mk_temp_dir(10)
    # del_temp_dir()
    # set_tmp_epoch()
    # print(get_tmp_epoch())
    # train({}, 0, "")
    # print(set_model(index=10))
    # print(get_model_list())
    # print(delete_model(index=10))
    pass
