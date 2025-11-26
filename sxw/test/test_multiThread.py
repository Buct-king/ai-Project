import threading

import time


# 这个函数名可随便定义
def run(n):
    time.sleep(5)
    print("current task：", n)


def test():
    t1 = threading.Thread(target=run, args=("thread 1",))
    t2 = threading.Thread(target=run, args=("thread 2",))
    t1.start()
    t2.start()
    return "test"


if __name__ == "__main__":
    print(test())