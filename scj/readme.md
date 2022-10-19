# 后端接口说明

## 软件初始化

代码位置：scj/code/initialization.py

### <code>get_root_path()</code>  获取存储结构的根目录

作用：获取存储内容的根目录，根目录具体存储位置未定，后续需要修改，暂时定位到：default_detection/dir_test

★重要：根据此目录可以获取系统配置文件system.ini

参数：无

返回值：根目录的绝对路径（string）

### <code>directory_ini()</code> 创建软件存储环境

作用：创建软件的存储环境、目录结构以及组织相关文件内容

参数：无

返回值：无

## 设备处理相关功能
代码位置：scj/code/device.py

### 视频功能函数

#### <code>video_judge(url_path)</code> 视频能否被打开判断函数
作用：判断传入的视频（地址）能否被正常读取

参数：<code>url_path</code> qurl格式的视频路径

返回值：int类型
```
1  # 错误码1，文件不存在
2  # 错误码2，文件类型错误
0  # 文件类型检查无误，可以打开
```

#### <code>history_video()</code> 获取历史视频列表

作用：获取历史检测过的全部视频

参数：无

返回值：json

```python
json = {
  "devices_cnt": 0,  # 历史视频的数量, int
  "devices_list": {
    # 历史视频列表list
    "device_name": "device_path"  # 键值对 key：设备/视频名 value：对应的存储目录位置
  }
}
```

#### <code> open_new_video(video_url_path)</code> 打开新视频

作用：打开新视频

参数：<code>video_url_path</code> 视频的qurl地址

返回值：
```python
json = {
    "code": -1,  # 状态码。-1表示无意义
    "message": "null",  # 状态码信息
    "video_name": "null",  # 视频名称
    "video_path": "null"  # 视频路径
}
# //状态码及含义
# //-1 无意义
# //0 Video already exists! 视频已经存在
# //1 OK 成功
```

#### <code>open_old_video(video_name)</code> 打开历史视频
作用：根据传入的视频名称（无.mp4后缀），判断并打开历史视频

参数：<code>video_name</code> 视频名称，无.mp4后缀

返回值：json
```python
json = {
    "code": -1,  # 状态码，-1表示无意义
    "message": "null",  # 状态码信息
    "video_name": "null",  # 视频名称
    "video_path": "null"  # 视频路径
}
# 状态码及含义
# -1 无意义
# 0 Video does not exist! 视频不存在
# 1 OK 成功
```

#### <code>get_video_information(video_name)</code> 获取视频信息

作用：获取视频信息

参数：<code>video_name</code> 视频名，string，无.mp4后缀

返回值：json
```python
json = {
    "video_name": 'string', # 视频名，有.mp4后缀
    "video_path": 'string', # 视频存储的绝对路径
    "video_size": "null", # 视频大小
    "last_visit": "null", # 最后一次访问时间
    "last_change": "null" # 最后一次修改时间
}
```

#### <code>get_pre_video(video_name)</code> 获取上一个视频

作用：获取上一个视频

参数：<code>video_name</code> 视频名称，无.mp4后缀

返回值：json
```python
json = {
    'code': 1,  # 状态码
    'message': 'null',  # 状态信息
    'video_name': 'null',  # 视频名称(无.mp4后缀)
    'video_path': 'null'  # 视频路径
}
# //状态码及含义
# //1 OK 上一个视频信息获取成功
# //-1 当前视频不存在
# //-2 已经是第一个视频
```

#### <code>get_next_video(video_name)</code> 获取下一个视频

作用：获取下一个视频

参数：<code>video_name</code> 视频名称，无.mp4后缀

返回值：json
```python
json = {
    "code": 1,  # 状态码
    "message": "null",  # 状态信息  
    "video_name": "null",  # 视频名称(无.mp4后缀)
    "video_path": "null"  # 视频路径
}
# //状态码及含义
# //1 OK 上一个视频信息获取成功
# //-1 当前视频不存在
# //-2 已经是第一个视频
```

### 视频工具函数

#### <code>qurl_to_string(url)</code> qurl转url

作用：将qurl格式转为url

参数：qurl类型的路径

返回值：url（string）

#### <code>format_byte(number)</code> 文件大小格式转换

#### <code>format_time(longtime)</code> 时间格式转换

### 摄像头功能函数

#### <code>get_camera_list()</code> 获取摄像头设备列表

作用：获取本地可调用的摄像头设备名称列表

参数：无

返回值：设备列表 json
```python
json = {
    'camera_num': 0,  # 设备可调用的摄像头数量
    'camera_list': []  # 设备列表，元素为_camera类型
}
_camera = {
    'id': -1,  # 摄像头id，opencv中调用的识别号
    'name': "string",  # 摄像头名字
    'status': "",  # 摄像头状态
    'size_height': -1,  # 画面高度
    'size_weight': -1  # 画面宽度
}
eg = {
    "camera_num": 1, 
    "camera_list": [
        {
            "id": 0, 
            "name": "<VideoCapture 0x7fcabc09bcf0>", 
            "status": "OK", 
            "size_height": 720.0, 
            "size_weight": 1280.0
        }
    ]
}
```

#### <code>history_camera()</code> 获取历史使用的摄像头列表

作用：获取历史曾使用过的摄像头列表，与视频类似

参数：无

返回值：历史设备列表，json

```python
json = {
    'devices_cnt': 0,  # 整数状态码，表示历史摄像头设备数量
    'devices_list': {  # 历史摄像头列表
        "device_name": "device_path"  # 键值对 key：设备/视频名 value：对应的存储目录位置
    }
}
# 状态码及其含义
# 0 ,摄像头创建失败，已经存在同名的摄像头
```


#### <code>open_new_camera(camera_name, camera_code)</code> 创建新摄像头

作用：创建新的摄像头（起别名，创建新的独立存储文件夹）

参数：<code>camera_name</code> 摄像头名称；<code>camera_code</code> 摄像头索引值（opencv），从0开始

返回值：创建动作结果，json

```python
json = {
    'code': -1,  # 状态码
    'message': "null",  # 状态码信息
    'camera_name': 'null',  # 摄像头名称
    'camera_path': 'null'  # 摄像头相关文件存储目录
}
'''
状态码及其含义
-1：camera present but does not open  摄像头不可用（不存在）
-2：camera present but does not reads 摄像头不可读取视频流的画面（摄像头异常或权限异常）
-3：Camera already exists! 摄像头已经存在（存在重名的摄像头，需要重新起名）
1： OK，创建成功
'''
```

#### <code>open_old_camera(camera_name)</code> 打开历史视频

作用：打开历史摄像头记录继续存储处理，切换当前处理的摄像头对象

参数：<code>camera_name</code> 视频名称

返回值：动作结果，json

```python
json = {
    'code': 0,  # 状态码
    'message': "null",  # 状态码信息
    'camera_name': 'null',  # 摄像头名称
    'camera_path': 'null'  # 摄像头相关文件存储目录
}
'''
状态码及其含义
0：Camera does not exist!  失败，摄像头不存在
1： OK，切换成功
'''
```