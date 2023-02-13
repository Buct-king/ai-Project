import ffmpy
# # 需要转换格式的视频文件，文件真实存在
# source_file = r"C:\Users\11795\Videos\testss.mp4"
# # 转换成功后的视频文件，文件夹真实存在，不会自动创建
# sink_file = r"C:\Users\11795\Videos\output_sss.mov"
#
# ff = ffmpy.FFmpeg(
#      inputs = {source_file: None},
#      outputs = {sink_file: None})
# ff.run()


def convertVideo(source_file,sink_file):
     """
     转换视频格式
     :param source_file: 源视频地址
     :param sink_file: 转换后视频地址
     """

     ff = ffmpy.FFmpeg(
          inputs={source_file: None},
          outputs={sink_file: None})
     ff.run()

