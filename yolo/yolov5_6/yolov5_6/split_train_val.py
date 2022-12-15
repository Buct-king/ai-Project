# coding:utf-8

import os
import random
import argparse
from xml_to_yolo import xml2yolo
import yaml


def to_yaml(dataset_path):
    yaml_name = os.path.join(dataset_path, 'mydata.yaml')

    trian_txt = os.path.join(dataset_path, 'tvt_txt/train.txt').replace('\\', '/')
    val_txt = os.path.join(dataset_path, 'tvt_txt/val.txt').replace('\\', '/')
    test_txt = os.path.join(dataset_path, 'tvt_txt/test.txt').replace('\\', '/')

    desired_caps = {'train': trian_txt,
                    'val': val_txt,
                    'test': test_txt,
                    'nc': 1,
                    'names': {0: "fault"}}

    with open(yaml_name, 'w', encoding='utf-8') as f:
        yaml.dump(desired_caps, f)


def stv(dataset_path):
    xml2yolo(dataset_path)

    trainval_percent = 1.0  # 训练集和验证集所占比例。 这里没有划分测试集
    train_percent = 0.9  # 训练集所占比例，可自己进行调整
    imagesfilepath = os.path.join(dataset_path, 'images')
    txtsavepath = os.path.join(dataset_path, 'tvt_txt')
    total_img_path = [os.path.join(imagesfilepath, x) for x in os.listdir(imagesfilepath)]

    if not os.path.exists(txtsavepath):
        os.makedirs(txtsavepath)

    num = len(total_img_path)
    list_index = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list_index, tv)
    train = random.sample(trainval, tr)

    file_trainval = open(txtsavepath + '/trainval.txt', 'w')
    file_test = open(txtsavepath + '/test.txt', 'w')
    file_train = open(txtsavepath + '/train.txt', 'w')
    file_val = open(txtsavepath + '/val.txt', 'w')

    for i in list_index:
        name = total_img_path[i] + '\n'
        if i in trainval:
            file_trainval.write(name)
            if i in train:
                file_train.write(name)
            else:
                file_val.write(name)
        else:
            file_test.write(name)

    file_trainval.close()
    file_train.close()
    file_val.close()
    file_test.close()
    to_yaml(dataset_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # xml文件的地址，根据自己的数据进行修改 xml一般存放在Annotations下
    parser.add_argument('--xml_path', default='Annotations', type=str, help='input xml label path')
    # 数据集的划分，地址选择自己数据下的ImageSets/Main
    parser.add_argument('--txt_path', default='ImageSets/Main', type=str, help='output txt label path')
    opt = parser.parse_args()

    trainval_percent = 1.0  # 训练集和验证集所占比例。 这里没有划分测试集
    train_percent = 0.9  # 训练集所占比例，可自己进行调整
    imagesfilepath = opt.xml_path
    txtsavepath = opt.txt_path
    total_img_path = os.listdir(imagesfilepath)
    if not os.path.exists(txtsavepath):
        os.makedirs(txtsavepath)

    num = len(total_img_path)
    list_index = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list_index, tv)
    train = random.sample(trainval, tr)

    file_trainval = open(txtsavepath + '/trainval.txt', 'w')
    file_test = open(txtsavepath + '/test.txt', 'w')
    file_train = open(txtsavepath + '/train.txt', 'w')
    file_val = open(txtsavepath + '/val.txt', 'w')

    for i in list_index:
        name = total_img_path[i][:-4] + '\n'
        if i in trainval:
            file_trainval.write(name)
            if i in train:
                file_train.write(name)
            else:
                file_val.write(name)
        else:
            file_test.write(name)

    file_trainval.close()
    file_train.close()
    file_val.close()
    file_test.close()
