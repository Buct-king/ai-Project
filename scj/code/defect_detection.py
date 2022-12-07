import cv2
import os
from configparser import ConfigParser
import scj.code.initialization as initialization
import json
import time
from scj.code.snapshot import new_snapshot
from yolo.yolov5_6.yolov5_6.detect import json_video_test
from scj.code.snapshot import new_snapshots
from scj.code.tool import get_system_ini


# 视频缺陷检测
# def video_defect_detection():
#     # 获取系统配置 conf
#     config_path = initialization.get_root_path() + "/system.ini"
#     conf = ConfigParser()
#     conf.read(config_path)
#     # 从conf获得当前正在处理的视频名称
#     video_name = conf.get("processing", "video")
#     video_dir_path = conf.get("path_config", "device_video_path") + "/" + video_name
#     original_video_path = video_dir_path + "/" + video_name + ".mp4"
#     new_video_path = video_dir_path + "/__" + video_name+"/"
#     json_ans = json_video_test(original_video_path, new_video_path)  # 调用
#     json_ans = json.loads(json_ans)
#     # json_ans = json_test(original_video_path, new_video_path)
#     defect_cnt = len(json_ans["fault_list"])
#     defects = json_ans["fault_list"]
#     cap = cv2.VideoCapture(original_video_path)
#     is_opened = cap.isOpened
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     defect_num = 0
#     frame_num = 1
#     while is_opened and defect_num < defect_cnt:
#         (flag, frame) = cap.read()  # 读取每一帧，flag表示是否读取成功，frame为图片内容
#         # print("frame:", frame_num, " defect:", defect_num)
#         while defect_num < defect_cnt and frame_num == defects[defect_num]["frame_num"]:
#             post_dict = {
#                 "origin_image": frame.tolist(),  # size(480*320)
#                 "poses": str(defects[defect_num]["position"]),  # [x1，y1，x2，y2]
#                 "time": time.asctime(),
#                 "video_time": defects[defect_num]["time"],  # (string)
#                 "note": "Recognized by AI",  # string
#                 "type": 0  # 0表示视频，1表示直播
#             }
#             dict_ = json.dumps(post_dict, ensure_ascii=False)
#             new_snapshot(dict_, defects[defect_num]["position"])
#             defect_num = defect_num + 1
#         if flag is not True:
#             break
#         frame_num += 1
#         # break
#     return new_video_path + video_name + ".mp4"


def video_defect_detection(video_path=""):
    # 获取系统配置 conf
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    # 从conf获得当前正在处理的视频名称
    video_name = conf.get("processing", "video")
    video_dir_path = conf.get("path_config", "device_video_path") + "/" + video_name
    if video_path != "":
        original_video_path = video_path
    else:
        original_video_path = video_dir_path + "/" + video_name + ".mp4"
    new_video_path = video_dir_path + "/__" + video_name+"/"
    # json_ans = json_test(original_video_path, new_video_path)  # 测试用
    json_ans = json_video_test(original_video_path, new_video_path)  # 调用
    json_ans = json.loads(json_ans)
    defect_cnt = len(json_ans["fault_list"])
    defects = json_ans["fault_list"]
    cap = cv2.VideoCapture(original_video_path)
    # 快照存储配置获取
    device_name = get_system_ini("video")  # 获取当前正在检测的视频名称
    store_path = get_system_ini("device_video_path") + "/" + device_name + "/images"  # 视频快照存储的文件
    image_list_path = store_path + "/image_list.yml"
    import yaml
    with open(image_list_path, 'r') as f:  # 读取image list的内容
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    with open(image_list_path, 'w+') as f:
        cnt = 0
        for defect in defects:
            cnt += 1
            print("processing [ %d / %d]" % (cnt, len(defects)))
            yml_dict["image_index"] = 1 + yml_dict["image_index"]
            yml_dict["image_num"] = 1 + yml_dict["image_num"]
            frame_idx = defect["frame_num"]
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx-1)
            flag, img = cap.read()
            img_pos = defect["position"]
            origin_image = img[img_pos[1]:img_pos[3], img_pos[0]:img_pos[2], :]
            time_now = time.localtime()
            time_str = time.strftime("%Y%m%d-%H_%M_%S", time_now)
            image_name = str(yml_dict["image_index"]) + "_" + device_name + "_" + str(time_str) + ".jpg"
            image_info = {
                "image_name": image_name,
                "image_time": time.strftime("%Y%m%d-%H_%M_%S", time_now),
                "image_note": "Recognized by AI",
                "video_time": defect["time"],
                "index": yml_dict["image_index"],
                "poses": str(defect["position"])
            }
            yml_dict["image_list"].append(image_info)
            cv2.imwrite(os.path.join(store_path, image_name), origin_image)
        yaml.dump(yml_dict, f, allow_unicode=True)
        f.close()
    # while is_opened and defect_num < defect_cnt:
    #     (flag, frame) = cap.read()  # 读取每一帧，flag表示是否读取成功，frame为图片内容
    #     while defect_num < defect_cnt and frame_num == defects[defect_num]["frame_num"]:
    #         img_pos = defects[defect_num]["position"]
    #         post_dict = {
    #             "origin_image": frame[img_pos[1]:img_pos[3], img_pos[0]:img_pos[2], :].tolist(),  # size(480*320)
    #             "poses": str(defects[defect_num]["position"]),  # [x1，y1，x2，y2]
    #             "time": time.asctime(),
    #             "video_time": defects[defect_num]["time"],  # (string)
    #             "note": "Recognized by AI",  # string
    #         }
    #         dict_ = json.dumps(post_dict, ensure_ascii=False)
    #         # new_snapshot(dict_, defects[defect_num]["position"])
    #         image_list['images'].append(post_dict)
    #         defect_num = defect_num + 1
    #     if flag is not True:
    #         break
    #     frame_num += 1
    #     # break
    # print("begin saving")
    # new_snapshots(json.dumps(image_list))
    return new_video_path + video_name + ".mp4"


def camera_defect_detection(image, detect_json):
    """
    :param image: 需要处理的图像帧
    :param detect_json: 检测出的缺陷json，格式同视频
    :return: 无
    """
    detect_json = json.loads(detect_json)
    for defect in detect_json["fault_list"]:
        post_dict = {
            "origin_image": image.tolist(),  # size(480*320)
            "poses": str(defect["position"]),  # [x1，y1，x2，y2]
            "time": time.asctime(),
            "video_time": defect["time"],  # (string)
            "note": "Recognized by AI",  # string
            "type": 1  # 0表示视频，1表示直播
        }
        dict_ = json.dumps(post_dict, ensure_ascii=False)
        new_snapshot(dict_, defect["position"])
    pass


def json_test(original_video_path, new_video_path):
    with open("./test/json_str.json", "r") as f:
        json_data = json.load(f)
        return json_data
    pass


def cap_test():
    cap = cv2.VideoCapture('/Users/shichunjing/code/python/labProjects/concrete/fault_detection/dir_test/data/device/video/test_vedio/test_vedio.mp4')  # 返回一个capture对象
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 设置要获取的帧号
    a, b = cap.read()  # read方法返回一个布尔值和一个视频帧。若帧读取成功，则返回True
    print(a)
    cv2.imwrite("/Users/shichunjing/Desktop/test.jpg", b)


if __name__ == '__main__':
    video_defect_detection()
    # cap_test()
    pass
