import cv2
import os
import platform
import sys


def translate_frame_rate(video_url,dist_url,rate=10):
    """
    转换视频到目标帧率
    :param video_url:
    :param dist_url:
    :param rate:
    :return:
    """


    cap = cv2.VideoCapture()
    cap.open(video_url)
    isOpened = cap.isOpened
    out = cv2.VideoWriter(dist_url,cv2.VideoWriter_fourcc(*'mp4v'),rate,(int(cap.get(3)), int(cap.get(4))))

    origin_rate = cap.get(cv2.CAP_PROP_FPS)
    origin_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    multi=int(origin_rate/rate)
    cnt=0
    print(multi)
    while isOpened:
        ret,frame=cap.read()
        print(ret)
        if ret:
            print(cnt)
            if cnt==0:
                print("int",cnt)
                out.write(frame)
        else:
            break
        cnt = (cnt + 1) % multi
    out.release()


# translate_frame_rate("C:\\Users\\11795\Videos\\test_.mp4","C:\\Users\\11795\Videos\\temp.mp4",10)

