import cv2
import math
import numpy as np
from scj.code.snapshot import delete_snapshot
from scj.code.tool import get_system_ini


def compare_images(image1, image2):
    # 计算图像的直方图
    hist1 = cv2.calcHist([image1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0, 256])
    # 计算直方图的相似度
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    # return similarity
    return True if similarity > 0.995 else False


def similarity_test():
    # 读入两张图片
    img1 = cv2.imread('/Users/shichunjing/Desktop/test1.png')
    img2 = cv2.imread('/Users/shichunjing/Desktop/test2.png')
    # 计算两张图片的相似度
    similarity = compare_images(img1, img2)
    print(similarity)
    # 根据相似度判断图片是否重复
    if similarity > 0.97:
        print("Images are duplicates")
    else:
        print("Images are not duplicates")


# 视频去重
def video_duplicate_remove(defect_dict, cap):
    defects = []
    for i in range(len(defect_dict)):
        if i == 0:
            defects.append(defect_dict[i])
        else:
            frame_idx = defect_dict[i]["frame_num"]
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx - 1)
            flag, img = cap.read()
            img_pos = defect_dict[i]["position"]
            new_image = img[img_pos[1]:img_pos[3], img_pos[0]:img_pos[2], :]
            l = len(defects)
            simi = False
            for j in range(l):
                idx = l - j - 1
                frame_idx = defects[idx]["frame_num"]
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx - 1)
                flag, img = cap.read()
                img_pos = defects[idx]["position"]
                _image = img[img_pos[1]:img_pos[3], img_pos[0]:img_pos[2], :]
                if compare_images(_image, new_image):
                    simi = True
                    break
            if simi is not True:
                defects.append(defect_dict[i])
    return defects


# 直播去重
def camera_duplicate_remove(camera_name):
    store_path = get_system_ini("device_camera_path") + "/" + camera_name + "/images"
    print("device_camera_path is "+get_system_ini("device_camera_path"))
    image_list_path = store_path + "/image_list.yml"
    import yaml
    with open(image_list_path, 'r') as f:  # 读取image list的内容
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    img_list = yml_dict['image_list']
    new_img_list = []
    for i in range(len(img_list)):
        if i == 0:
            new_img_list.append(img_list[i])
        else:

            print(store_path + '/'+img_list[i]['image_name'])
            img = cv2.imread(store_path + '/'+img_list[i]['image_name'])
            l = len(new_img_list)
            simi = False
            for j in range(l):
                idx = l - j - 1
                img2 = cv2.imread(store_path + '/'+new_img_list[idx]['image_name'])
                if compare_images(img, img2):
                    simi = True
                    break
            if simi is not True:
                new_img_list.append(img_list[i])
            else:
                delete_snapshot(img_list[i]['index'], 1)
    pass


def video_duplicate_remove_2(video_name):
    store_path = get_system_ini("device_video_path") + "/" + video_name + "/images"
    print("device_video_path is "+get_system_ini("device_video_path"))
    image_list_path = store_path + "/image_list.yml"
    import yaml
    with open(image_list_path, 'r') as f:  # 读取image list的内容
        yml_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    img_list = yml_dict['image_list']
    new_img_list = []
    for i in range(len(img_list)):
        if i == 0:
            new_img_list.append(img_list[i])
        else:

            print(store_path + '/'+img_list[i]['image_name'])
            img = cv2.imread(store_path + '/'+img_list[i]['image_name'])
            l = len(new_img_list)
            simi = False
            for j in range(l):
                idx = l - j - 1
                img2 = cv2.imread(store_path + '/'+new_img_list[idx]['image_name'])
                if compare_images(img, img2):
                    simi = True
                    break
            if simi is not True:
                new_img_list.append(img_list[i])
            else:
                delete_snapshot(img_list[i]['index'], 0)
    pass