"""
生产者与消费者：
    两个线程之间的通信
    import queue
    queue.put()
    queue.get()
"""
import random
from multiprocessing import Queue
from threading import Thread
from time import sleep


def task1(q):
    n = 1
    while n < 5:
        q.put(n)
        print('张三正在做第%d个包子!' % n)
        n += 1
        sleep(3)


def task2(q):
    for i in range(4):
        n = q.get()
        print('李四正在吃第%d个包子' % n)
        # q.task_done()
        sleep(1)


if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=task1, args=(q,))
    t2 = Thread(target=task2, args=(q,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('-------END--------')
