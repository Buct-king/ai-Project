import xml.dom.minidom
import os

path = r'C:\Users\11795\Documents\WeChat Files\wxid_ihlhv1mvzrx122\FileStorage\File\2023-01\Desktop\网上标准数据集标注'  # xml文件存放路径
sv_path = r'G:\Lab_work\fault_detection_new\dataset\xmls'  # 修改后的xml文件存放路径
files = os.listdir(path)
cnt = 0

for xmlFile in files:
    dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  # 打开xml文件，送到dom解析
    root = dom.documentElement  # 得到文档元素对象
    item = root.getElementsByTagName('path')  # 获取path这一node名字及相关属性值
    for i in item:
        temp=i.firstChild.data[-10:]
        print(temp)
        i.firstChild.data = r'G:\Lab_work\fault_detection_new\dataset\images' + temp # xml文件对应的图片路径

    with open(os.path.join(sv_path, xmlFile), 'w', encoding='utf-8') as fh:
        dom.writexml(fh)
