# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
from os import getcwd

import glob

def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_annotation(xmls_path, labels_path):
    classes = ["fault"]  # 改成自己的类别

    in_file = open(xmls_path, encoding='UTF-8')
    out_file_name = f'{labels_path}/{os.path.basename(xmls_path)[:-4]}.txt'

    out_file = open(out_file_name, 'a')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        # difficult = obj.find('Difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        # 标注越界修正
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


def xml2yolo(dataset_path):
    xmls_path = os.path.join(dataset_path, 'xmls')
    labels_path = os.path.join(dataset_path, 'labels')
    xmls = glob.glob(f'{xmls_path}/*.xml')
    for xmls_path in xmls:
        convert_annotation(xmls_path, labels_path)

