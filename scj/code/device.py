# -*- coding: utf-8 -*-
import os
from configparser import ConfigParser
import scj.code.initialization as initialization
import shutil
import json
import time
import yaml
import cv2


# qurl转string
def qurl_to_string(url):
    s = url.toString()
    return s[8:]


def format_byte(number):
    for(scale, label) in [(1024*1024*1024, "GB"), (1024*1024, "MB"), (1024, "KB")]:
        if number >= scale:
            return "%.2f %s" % (number * 1.0 / scale, label)
        elif number == 1:
            return "1 字节"
        else:
            byte = "%.2f " % (number or 0)
    return (byte[:-3] if byte.endswith("00") else byte)+"字节"


def format_time(longtime):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(longtime))


# 视频文件打开判断
def video_judge(url_path):
    path = qurl_to_string(url_path)
    if os.path.isfile(path) is not True:
        return 1  # 错误码1，文件不存在
    if ".mp4" not in path:
        return 2  # 错误码2，文件类型错误
    return 0  # 文件类型检查无误，可以打开


# 获取历史视频列表 ====
def history_video():  # 获取历史检测过的视频/设备列表
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    path = conf.get("path_config", "device_video_path")
    all_devices = {}
    with open(initialization.get_root_path() + "/data/device_list.yml", 'r') as f:
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        devices_cnt = yml_dict["video"]["video_num"]
        for device in yml_dict["video"]["video_list"]:
            all_devices[device] = path + "/" + device
        f.close()
    json_dict = {
        'devices_cnt': devices_cnt,
        'devices_list': all_devices
    }
    return json.dumps(json_dict, ensure_ascii=False)


# 打开新视频
def open_new_video(video_url_path):  # 打开新视频时，调用该函数为视频创建视频内容保存路径
    video_path = qurl_to_string(video_url_path)
    # video_path = "aaaa/bbbb/cccc/dddd/abcd.mp4"  # 测试用
    # video_path = "/Users/shichunjing/Desktop/C++Primer.pdf"  # 测试用
    # video_path = "/Users/shichunjing/Desktop/STL源码剖析.pdf"
    return_dict = {
        'code': -1,  # 状态码，-1表示无意义
        'message': "null",  # 状态码信息
        'video_name': 'null',  # 视频名称
        'video_path': 'null'  # 视频路径
    }
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    # device_path = conf.get("path_config", "device_path")
    device_video_path = conf.get("path_config", "device_video_path")
    video_name = ""  # 视频名称
    i = len(video_path) - 1
    while i >= 0:
        if video_path[i] == '/':
            break
        video_name = video_path[i] + video_name
        i = i - 1
    history_video_dict = history_video()
    if history_video_dict.__contains__(video_name[:-4]):  # 新视频创建失败，已经存在相同名字的历史视频
        return_dict['code'] = 0
        return_dict['message'] = "Video already exists!"
        return json.dumps(return_dict)
    else:  # 为新视频创建存储路径
        video_status = os.stat(video_path)  # 获取视频信息状态
        new_device_information_dict = {  # 新视频需要存储的信息内容
            'video_name': video_name[:-4],
            'image_path': device_video_path + "/" + video_name[:-4] + "/images",
            'image_info': device_video_path + "/" + video_name[:-4] + "/images/image_list.yml",
            'video_info': {
                'original_path': video_path,
                'video_path': device_video_path + "/" + video_name[:-4],
                'video_size': format_byte(video_status.st_size),
                'last_visit': format_time(video_status.st_atime),
                'last_change': format_time(video_status.st_mtime)
            }
        }
        os.mkdir(device_video_path + "/" + video_name[:-4])
        os.mkdir(device_video_path + "/" + video_name[:-4] + "/images")
        with open(device_video_path + "/" + video_name[:-4] + "/" + video_name[:-4] + ".yml", 'a') as f:
            # yaml_data = yaml.load(f, Loader=yaml.FullLoader)
            yaml.dump(new_device_information_dict, f, allow_unicode=True)
            f.close()
        shutil.copyfile(video_path, device_video_path + "/" + video_name[:-4] + "/" + video_name)  # 复制视频副本
        conf.set('processing', 'video', video_name[:-4])  # 配置文件修改：当前正在处理的视频是该视频
        with open(initialization.get_root_path() + "/system.ini", 'w') as f:
            conf.write(f)
            f.close()
        return_dict['code'] = 1
        return_dict['message'] = "OK"
        return_dict['video_name'] = video_name[:-4]
        return_dict['video_path'] = device_video_path + "/" + video_name[:-4]
        # 向device_list文件中写入
        yml_dict = {}
        with open(initialization.get_root_path() + "/data/device_list.yml", 'r') as f:
            yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
            f.close()
        with open(initialization.get_root_path() + "/data/device_list.yml", 'w+') as f:
            yml_dict['video']['video_num'] = 1 + int(yml_dict['video']['video_num'])
            yml_dict['video']['video_list'].append(video_name[:-4])
            yaml.dump(yml_dict, f, allow_unicode=True)
            f.close()
        print(video_name[:-4])
        return json.dumps(return_dict, ensure_ascii=False)


# 打开历史视频
def open_old_video(video_name):
    return_dict = {
        'code': -1,  # 状态码，-1表示无意义
        'message': "null",  # 状态码信息
        'video_name': 'null',  # 视频名称
        'video_path': 'null'  # 视频路径
    }
    history_video_dict = history_video()
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    device_video_path = conf.get("path_config", "device_video_path")
    # print(history_video_dict)
    if history_video_dict.__contains__(video_name) is not True:  # 失败，视频不存在
        return_dict['code'] = 0
        return_dict['message'] = "Video does not exist!"
        return_dict['video_name'] = video_name
        return_dict['video_path'] = "null"
        return json.dumps(return_dict)
    else:
        return_dict['code'] = 1
        return_dict['message'] = "OK"
        return_dict['video_name'] = video_name
        return_dict['video_path'] = device_video_path + "/" + video_name
        conf.set('processing', 'video', video_name)
        with open(initialization.get_root_path() + "/system.ini", 'w') as f:
            conf.write(f)
            f.close()
        return json.dumps(return_dict, ensure_ascii=False)


# 获取视频信息
def get_video_information(video_name):
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    device_video_path = conf.get("path_config", "device_video_path")
    information_dict = {
        'video_name': video_name + ".mp4",
        'video_path': device_video_path + "/" + video_name + "/" + video_name + ".mp4",
        'video_size': "null",
        'last_visit': "null",
        'last_change': "null"
    }
    with open(device_video_path + "/" + video_name + "/" + video_name + ".yml", 'r') as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        information_dict['video_size'] = yaml_data['video_info']['video_size']
        information_dict['last_visit'] = yaml_data['video_info']['last_visit']
        information_dict['last_change'] = yaml_data['video_info']['last_change']
        f.close()
    return json.dumps(information_dict, ensure_ascii=False)


# 获取上一个视频
def get_pre_video(video_name):
    ans_dict = {
        'code': 1,
        'message': 'null',
        'video_name': 'null',
        'video_path': 'null'
    }
    history_list = json.loads(history_video())
    if history_list['devices_list'].__contains__(video_name) is not True:
        ans_dict['code'] = -1
        ans_dict['message'] = '视频不存在'
        return ans_dict
    for device in history_list['devices_list']:
        if device == video_name:
            if ans_dict['video_name'] == 'null':
                ans_dict['code'] = -2
                ans_dict['message'] = '已经是第一个视频'
            else:
                ans_dict['code'] = 1
                ans_dict['message'] = 'OK'
            break
        ans_dict['video_name'] = device
        ans_dict['video_path'] = history_list['devices_list'][device]
    return json.dumps(ans_dict, ensure_ascii=False)


# 获取下一个视频
def get_next_video(video_name):
    ans_dict = {
        'code': 1,
        'message': 'null',
        'video_name': 'null',
        'video_path': 'null'
    }
    history_list = json.loads(history_video())
    if history_list['devices_list'].__contains__(video_name) is not True:
        ans_dict['code'] = -1
        ans_dict['message'] = '视频不存在'
        return ans_dict
    file_has_found = False
    for device in history_list['devices_list']:
        if file_has_found is True:
            ans_dict['code'] = 1
            ans_dict['message'] = 'OK'
            ans_dict['video_name'] = device
            ans_dict['video_path'] = history_list['devices_list'][device]
            break
        if device == video_name:
            file_has_found = True
    if ans_dict['video_name'] == 'null':
        ans_dict['code'] = -2
        ans_dict['message'] = '已经是最后一个视频'
    return json.dumps(ans_dict, ensure_ascii=False)


# 获取可用的摄像头列表
def get_camera_list():
    is_working = True
    dev_port = 0
    camera_info = {
        'camera_num': 0,
        'camera_list': []
    }
    while is_working:
        camera = cv2.VideoCapture(dev_port)
        if not camera.isOpened():
            is_working = False
        else:
            _camera = {
                'id': dev_port,
                'name': str(camera),
                'status': "",
                'size_height': -1,
                'size_weight': -1
            }
            is_reading, img = camera.read()
            _camera['size_weight'] = camera.get(3)
            _camera['size_height'] = camera.get(4)
            if is_reading:
                _camera['status'] = "OK"
            else:
                _camera['status'] = "camera present but does not reads"
            camera_info['camera_list'].append(_camera)
        dev_port += 1
    camera_info['camera_num'] = dev_port - 1
    return json.dumps(camera_info, ensure_ascii=False)


# 创建新的摄像头设备
def open_new_camera(camera_name):

    pass


if __name__ == '__main__':
    # print(video_judge("xxx.mp4"))
    # print(history_video())
    # print(open_new_video(""))
    # print(open_old_video("C++Primer"))
    # get_file_information("/Users/shichunjing/Desktop/C++Primer.pdf")
    # print(get_video_information("C++Primer"))
    # print(get_pre_video("abcd"))
    # print(get_next_video("device_2_without_file"))
    # print(qurl_to_string(""))
    # get_camera_list()
    # print(get_camera_list())
    pass

