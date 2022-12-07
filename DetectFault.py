import os

root = os.getcwd()
python_path=os.path.join(root, "lib\\pyqt5\python.exe")
main_path=os.path.join(root, "main.py")
command =python_path+" "+main_path

os.system(command)