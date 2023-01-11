import os
import time
import cv2
import numpy as np
import yaml
from scj.code.tool import get_system_ini
import json
import os
import xlwt


# 添加新的快照
def new_snapshot(json_info, img_pos=[]):
    info = json.loads(json_info)
    image = info["origin_image"]
    if info["type"] == 0:
        device_name = get_system_ini("video")
        store_path = get_system_ini("device_video_path") + "/" + device_name + "/images"
    else:
        device_name = get_system_ini("camera")
        store_path = get_system_ini("device_camera_path") + "/" + device_name + "/images"
    image_list_path = store_path + "/image_list.yml"
    with open(image_list_path, 'r') as f:  # 读取image list的内容
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    with open(image_list_path, 'w+') as f:  # 修改image list
        yml_dict["image_index"] = 1 + yml_dict["image_index"]
        yml_dict["image_num"] = 1 + yml_dict["image_num"]
        time_now = time.localtime()
        time_str = time.strftime("%Y%m%d-%H_%M_%S", time_now)
        # print(time_str)
        image_name = str(yml_dict["image_index"]) + "_" + device_name + "_" + str(time_str) + ".jpg"
        image_info = {
            "image_name": image_name,
            "image_time": time.strftime("%Y%m%d-%H_%M_%S", time_now),
            "image_note": info["note"],
            "video_time": info["video_time"],
            "index": yml_dict["image_index"],
            "poses": info["poses"]
        }
        yml_dict["image_list"].append(image_info)
        yaml.dump(yml_dict, f, allow_unicode=True)
        f.close()
    image = np.array(image)
    # print(img_pos)
    # print(image.shape)
    _image = image[img_pos[1]:img_pos[3], img_pos[0]:img_pos[2], :]
    # print(_image.shape)
    cv2.imwrite(os.path.join(store_path, image_name), _image)
    return get_image_list(info["type"])


# 添加一组新的快照
def new_snapshots(json_info):
    info = json.loads(json_info)
    if len(info["images"]) == 0:
        return
    if info["type"] == 0:
        device_name = get_system_ini("video")
        store_path = get_system_ini("device_video_path") + "/" + device_name + "/images"
    else:
        device_name = get_system_ini("camera")
        store_path = get_system_ini("device_camera_path") + "/" + device_name + "/images"
    image_list_path = store_path + "/image_list.yml"
    print("读取image_list_path", time.time())
    with open(image_list_path, 'r') as f:  # 读取image list的内容
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    print("开始修改image_list_path", time.time())
    with open(image_list_path, 'w+') as f:  # 修改image list
        for img in info['images']:
            # print(yml_dict["image_index"])
            yml_dict["image_index"] = 1 + yml_dict["image_index"]
            yml_dict["image_num"] = 1 + yml_dict["image_num"]
            time_now = time.localtime()
            time_str = time.strftime("%Y%m%d-%H_%M_%S", time_now)
            image_name = str(yml_dict["image_index"]) + "_" + device_name + "_" + str(time_str) + ".jpg"
            image_info = {
                "image_name": image_name,
                "image_time": time.strftime("%Y%m%d-%H_%M_%S", time_now),
                "image_note": img["note"],
                "video_time": img["video_time"],
                "index": yml_dict["image_index"],
                "poses": img["poses"]
            }
            yml_dict["image_list"].append(image_info)
            image = np.array(img["origin_image"])
            cv2.imwrite(os.path.join(store_path, image_name), image)
        print("开始保存", time.time())
        yaml.dump(yml_dict, f, allow_unicode=True)
        f.close()
    print("全部完成", time.time())
    # print("over")
    # return get_image_list(info["type"])
    return


# 获取快照列表
def get_image_list(device_type):
    """
    :param device_type: 设备类型
    :return:
    """
    if device_type == 0:
        device_name = get_system_ini("video")
        store_path = get_system_ini("device_video_path") + "/" + device_name + "/images"
    else:
        device_name = get_system_ini("camera")
        store_path = get_system_ini("device_camera_path") + "/" + device_name + "/images"
    image_list_path = store_path + "/image_list.yml"
    with open(image_list_path, 'r') as f:  # 读取image list的内容
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    return json.dumps(yml_dict, ensure_ascii=False)


# 获取图像（快照）详情信息
def get_image_info(device_type, index):
    """
    :param device_type: 设备类型，0视频，1摄像头
    :param index: 快照id
    :return: info
    """
    if device_type == 0:
        device_name = get_system_ini("video")
        store_path = get_system_ini("device_video_path") + "/" + device_name + "/images"
    else:
        device_name = get_system_ini("camera")
        store_path = get_system_ini("device_camera_path") + "/" + device_name + "/images"
    image_list_path = store_path + "/image_list.yml"
    with open(image_list_path, 'r') as f:  # 读取image list的内容
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    img_list = yml_dict["image_list"]
    return_dict = {
        "code": 0,
        "message": "None",
        "info": {
            "image_name": "",
            "image_note": "",
            "image_time": "",
            "index": -1,
            "poses": '[, , , ]',
            "video_time": '',
            "image_path": ""
        }
    }
    for img in img_list:
        if img["index"] == index:
            return_dict["code"] = 1
            return_dict["message"] = "ok"
            return_dict["info"]["image_name"] = img["image_name"]
            return_dict["info"]["image_note"] = img["image_note"]
            return_dict["info"]["image_time"] = img["image_time"]
            return_dict["info"]["index"] = img["index"]
            return_dict["info"]["poses"] = img["poses"]
            return_dict["info"]["video_time"] = img["video_time"]
            return_dict["info"]["image_path"] = store_path + "/" + img["image_name"]
            break
    return json.dumps(return_dict, ensure_ascii=False)


# 修改快照内容
def modify_snapshot_info(device_type, index, index_=-1, image_note=""):
    """
    :param index: 快照原来的index
    :param index_: 希望修改的index
    :param image_note: 希望修改的图像备注
    :return:
    """
    if device_type == 0:
        device_name = get_system_ini("video")
        store_path = get_system_ini("device_video_path") + "/" + device_name + "/images"
    else:
        device_name = get_system_ini("camera")
        store_path = get_system_ini("device_camera_path") + "/" + device_name + "/images"
    image_list_path = store_path + "/image_list.yml"
    with open(image_list_path, 'r') as f:  # 读取image list的内容
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    img_list = yml_dict["image_list"]
    res_dict = {
        "code": -1,
        "message": "index error"
    }
    idx_set = set()
    for img in img_list:
        idx_set.add(img["index"])
    if index not in idx_set:
        return json.dumps(res_dict, ensure_ascii=False)
    if index_ in idx_set:
        res_dict["code"] = -2
        res_dict["message"] = "Failed to reset index"
        return json.dumps(res_dict, ensure_ascii=False)
    for img in yml_dict["image_list"]:
        if img["index"] == index:
            if image_note != "":
                img["image_note"] = image_note
            if index_ != -1:
                img["index"] = index_
            res_dict["code"] = 1
            res_dict["message"] = "OK"
            with open(image_list_path, 'w+') as f:  # 修改image list
                yaml.dump(yml_dict, f, allow_unicode=True)
                f.close()
    return json.dumps(res_dict, ensure_ascii=False)


# 删除快照
def delete_snapshot(index, device_type):
    if device_type == 0:
        device_name = get_system_ini("video")
        store_path = get_system_ini("device_video_path") + "/" + device_name + "/images"
    else:
        device_name = get_system_ini("camera")
        store_path = get_system_ini("device_camera_path") + "/" + device_name + "/images"
    image_list_path = store_path + "/image_list.yml"
    with open(image_list_path, 'r') as f:  # 读取image list的内容
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    res_dict = {
        "code": -1,
        "message": "index error"
    }
    for img in yml_dict["image_list"]:
        if img["index"] == index:
            os.remove(store_path + "/" + img["image_name"])
            yml_dict["image_list"].remove(img)
            with open(image_list_path, 'w+') as f:  # 修改image list
                yaml.dump(yml_dict, f, allow_unicode=True)
                f.close()
            return get_image_list(device_type)
    return get_image_list(device_type)


# 导出快照列表
def export_snapshot_list(device_type, snapshot_id_list=[], file_path=""):
    """
    :param device_type: 设备类型，0视频，1摄像头
    :param snapshot_id_list: 希望导出的快照id，默认为空
    :param file_path: 希望导出的文件存储的位置，默认存储在快照文件夹
    :return: json
    """
    if device_type == 0:
        device_name = get_system_ini("video")
        store_path = get_system_ini("device_video_path") + "/" + device_name + "/images/"
    else:
        device_name = get_system_ini("camera")
        store_path = get_system_ini("device_camera_path") + "/" + device_name + "/images/"
    image_list_path = store_path
    if file_path != "":
        store_path = file_path
    work_book = xlwt.Workbook(encoding='utf-8')
    sheet = work_book.add_sheet('缺陷检测结果')
    # 设备信息
    device_type_name = "视频" if device_type == 0 else "摄像头"
    sheet.write(0, 0, '设备类型：')
    sheet.write(0, 1, device_type_name)
    sheet.write(0, 2, "设备名称：")
    sheet.write(0, 3, device_name)
    # 统计信息
    sheet.write(1, 0, "导出快照图像数量：")
    sheet.write(1, 1, str(len(snapshot_id_list)))
    # 表头设置
    sheet.write(2, 0, "快照id")
    sheet.write(2, 1, "快照获取时间")
    sheet.write(2, 2, "视频/摄像头内时间")
    sheet.write(2, 3, "快照备注")
    sheet.write(2, 4, "快照超链接")
    # 详情信息
    sheet_lines = 3
    with open(image_list_path + "/image_list.yml", 'r') as f:  # 读取image list的内容
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    img_list = yml_dict["image_list"]
    for img in img_list:
        if img["index"] in snapshot_id_list:
            sheet.write(sheet_lines, 0, str(img["index"]))
            sheet.write(sheet_lines, 1, img["image_time"])
            sheet.write(sheet_lines, 2, img["video_time"])
            sheet.write(sheet_lines, 3, img["image_note"])
            sheet.write(sheet_lines, 4, xlwt.Formula('HYPERLINK("{}"; "{}")'.format(
                                            image_list_path + "/" + img["image_name"],
                                            img["image_name"])))
            sheet_lines += 1
    work_book.save(store_path + device_type_name + "_" + device_name + '_缺陷检测结果.xls')
    return_dict = {
        "code": 1,
        "message": "ok",
        "file_path": store_path + device_type_name + "_" + device_name + '_缺陷检测结果.xls'
    }
    return json.dumps(return_dict, ensure_ascii=False)

# 批量删除快照
def delete_snapshot_list(indexes, device_type):
    """
    :param indexes: 快照的id`列表`
    :param device_type: 设备类型，0表示视频，1表示摄像头
    :return: 新的快照列表
    """
    if device_type == 0:
        device_name = get_system_ini("video")
        store_path = get_system_ini("device_video_path") + "/" + device_name + "/images"
    else:
        device_name = get_system_ini("camera")
        store_path = get_system_ini("device_camera_path") + "/" + device_name + "/images"
    image_list_path = store_path + "/image_list.yml"
    with open(image_list_path, 'r') as f:  # 读取image list的内容
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    for img in yml_dict["image_list"]:
        if img["index"] in indexes:
            os.remove(store_path + "/" + img["image_name"])
            yml_dict["image_list"].remove(img)
    with open(image_list_path, 'w+') as f:  # 修改image list
        yaml.dump(yml_dict, f, allow_unicode=True)
        f.close()
    return get_image_list(device_type)


if __name__ == '__main__':
    post_dict = {
        "origin_image": cv2.imread("/Users/shichunjing/Pictures/1.jpeg").tolist(),  # size(480*320)
        "poses": "poses",  # [x1，y1，x2，y2]
        "time": time.asctime(),
        "video_time": "self.snapshotVideoTime",  # (string)
        "note": "note",  # string
        "type": 0  # 0表示视频，1表示直播
    }
    dict_ = json.dumps(post_dict, ensure_ascii=False)
    # im = cv2.imread("/Users/shichunjing/Pictures/1.jpeg")
    # print(new_snapshot(dict_))
    # print(get_image_list(0))

    # print(modify_snapshot_info(0, 2, index_=-1, image_note="note test"))

    # print(delete_snapshot(2, 1))
    # print(get_image_info(0, 2))
    export_snapshot_list(0, [1,2,3,4,5,6,7,8,9])
    pass
