import cv2
import os
from configparser import ConfigParser
import scj.code.initialization as initialization
import json
import time
from scj.code.snapshot import new_snapshot
from yolo.yolov5_6.yolov5_6.detect import json_video_test

# 视频缺陷检测
def video_defect_detection():
    # 获取系统配置 conf
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    # 从conf获得当前正在处理的视频名称
    video_name = conf.get("processing", "video")
    video_dir_path = conf.get("path_config", "device_video_path") + "/" + video_name
    original_video_path = video_dir_path + "/" + video_name + ".mp4"
    new_video_path = video_dir_path + "/__" + video_name+"/"
    json_ans = json_video_test(original_video_path, new_video_path)  # 调用
    json_ans=json.loads(json_ans)
    # json_ans = json_test(original_video_path, new_video_path)
    defect_cnt = len(json_ans["fault_list"])
    defects = json_ans["fault_list"]
    cap = cv2.VideoCapture(original_video_path)
    is_opened = cap.isOpened
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    defect_num = 0
    frame_num = 1
    while is_opened and defect_num < defect_cnt:
        (flag, frame) = cap.read()  # 读取每一帧，flag表示是否读取成功，frame为图片内容
        # print("frame:", frame_num, " defect:", defect_num)
        while defect_num < defect_cnt and frame_num == defects[defect_num]["frame_num"]:
            post_dict = {
                "origin_image": frame.tolist(),  # size(480*320)
                "poses": str(defects[defect_num]["position"]),  # [x1，y1，x2，y2]
                "time": time.asctime(),
                "video_time": defects[defect_num]["time"],  # (string)
                "note": "Recognized by AI",  # string
                "type": 0  # 0表示视频，1表示直播
            }
            dict_ = json.dumps(post_dict, ensure_ascii=False)
            new_snapshot(dict_, defects[defect_num]["position"])
            defect_num = defect_num + 1
        if flag is not True:
            break
        frame_num += 1
        # break
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
    with open("G:\Lab_work\\fault_detection_new\\fault_detection\scj\code\\test\json_str.json", "r") as f:
        json_data = json.load(f)
        return json_data
    pass


if __name__ == '__main__':
    video_defect_detection()
    pass
