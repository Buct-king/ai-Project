# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import numpy as np
import math
import json


def calParallelLineDistance(line1, line2):
    """
    计算平行线间的像素距离
    :param line1:
    :param line2:
    :return:
    """
    x1, y1, x2, y2 = line1[0]
    a1, b1, a2, b2 = line2[0]
    if math.isclose(x1, x2) and math.isclose(a1, a2):
        return a2 - x1, True

    A = y2 - y1
    B = x1 - x2
    C1 = x2 * y1 - x1 * y2
    C2 = a2 * b1 - a1 * b2
    return math.fabs(C2 - C1) / math.sqrt(A * A + B * B), True


def calDistance(image=None, image_path=None):
    """
    计算激光标尺间的像素距离
    :param image:
    :param image_path:
    :return:
    """
    LASER_SCALE = 1000

    # return_json = {
    #     "code": 0,
    #     "message": "success to calculate distance.",
    #     "distance": None
    # }
    if image is None and image_path is None:
        # return_json["message"] = "failed！No valid image object or image path。"
        return 1
    if image_path is not None:
        image = cv2.imread(image_path)
    # 读进来的图像格式是BGR
    thres = int(min(image.shape[0] / 2, image.shape[1] / 2))
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 颜色在HSV空间下的上下限156-180还能改成0-10
    low_hsv = np.array([156, 43, 46])
    high_hsv = np.array([180, 255, 255])

    # 使用opencv的inRange函数提取颜色
    mask = cv2.inRange(imgHSV, lowerb=low_hsv, upperb=high_hsv)
    lines = cv2.HoughLinesP(mask, 1, np.pi / 180, threshold=thres, maxLineGap=200)

    if len(lines) < 2:
        # return_json["message"] = "failed！Laser line not recognized。"
        # result = json.dumps(return_json)
        return 1

    res = []
    for i, line1 in enumerate(lines):
        for j, line2 in enumerate(lines):
            if i == j:
                continue
            value, flag = calParallelLineDistance(line1, line2)
            if flag:
                res.append(value)

    print(int(np.max(np.array(res))))

    distance_pix = int(np.max(np.array(res)))
    if len(res) == 0:
        # return_json["message"] = "failed! recognize error。"
        # result = json.dumps(return_json)
        return 1
    else:
        # return_json["message"] = "success!"
        # return_json["code"] = 1
        # return_json["distance"] = int(np.max(np.array(res)))
        # result = json.dumps(return_json)
        return LASER_SCALE / distance_pix


calDistance(image_path="image (741).jpg")

#
# def main():
#     img = cv2.imread("image (741).jpg")
#
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
#     # 颜色在HSV空间下的上下限156-180还能改成0-10
#     low_hsv = np.array([156, 43, 46])
#     high_hsv = np.array([180, 255, 255])
#
#     # 使用opencv的inRange函数提取颜色
#     edges = cv2.inRange(imgHSV, lowerb=low_hsv, upperb=high_hsv)
#
#     # img = cv2.imread("img.png")
#     # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # edges = cv2.Canny(gray, 50, 200)
#     # print(edges)
#     # exit()
#     lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30)
#     lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=500, maxLineGap=200)
#     # cv2.imwrite("gray.png",gray)
#     cv2.imwrite("edges.png", edges)
#     print(len(lines))
#     for line in lines:
#         x1, y1, x2, y2 = line[0]
#         cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0))
#         # cv2.imshow('img', img)
#
#     cv2.imwrite("img_ed.jpg", img)
#     # if cv2.waitKey(0) == ord('q'):
#     #     cv2.destroyAllWindows()
#
#
# if __name__ == '__main__':
#     main()
