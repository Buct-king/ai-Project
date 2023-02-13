import os

filePath=r"G:\Lab_work\fault_detection_new\dataset\labels"
imagePath=r"G:\Lab_work\fault_detection_new\dataset\images"
images=os.listdir(filePath)
imagess=os.listdir(imagePath)
images=[x[:-4] for x in images]
print(images)
print(imagess)

for x in imagess:
    if x[:-4] not in images:
        os.remove(os.path.join(imagePath,x))
