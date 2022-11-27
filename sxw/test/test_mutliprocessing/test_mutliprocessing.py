from queue import Queue
import random, threading, time
from func import test_f,test_m
# 生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue
    def run(self):
        while True:
            print("生产者 %s 将产品加入队列" % (self.getName()))
            test_f()
            self.data.put("tst")
            time.sleep(5)
        print("生产者 %s 完成" % self.getName())

# 消费者类
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue
    def run(self):
        while True:
            val = self.data.get()
            test_m()
            print("消费者 %s 将产品从队列中取出" % (self.getName()))
            time.sleep(random.random())
        print("消费者 %s 完成" % self.getName())

if __name__ == '__main__':
    print("---主线程开始---")
    queue = Queue()                         # 实例化队列
    producer = Producer("Producer", queue)  # 实例化线程 Producer，并传入队列作为参数
    consumer = Consumer("Consumer", queue)  # 实例化线程 Consumer，并传入队列作为参数
    producer.start()                        # 启动线程 Producer
    consumer.start()                        # 启动线程 Consumer
    producer.join()                         # 等待线程 Producer 结束
    consumer.join()                         # 等待线程 Consumer 结束
    print("---主线程结束---")
