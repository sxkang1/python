"""
多线程：  多线程默认是有全局解释器锁的
    多线程默认是有全局解释器锁的，只是针对数据运算量小的情况
    运算量大的情况下  锁就不管用了，所以如果数据运算量大的情况下，建议用进程  或者 加锁

    lock = threading.Lock()
     lock.acquire() # 加锁 同步
     需要执行加锁的代码
     共享数据
     lock.release() # 释放锁
"""
import threading
from threading import Thread
from time import sleep

lock = threading.Lock()
list1 = [0] * 10000


def task1():
    for i in range(len(list1)):
        lock.acquire()
        list1[i] = 1
        sleep(.5)
        print('--->i:', i)
        lock.release()


def task2():
    lock.acquire()
    print(list1)
    lock.release()


if __name__ == '__main__':
    t1 = Thread(target=task1)
    t2 = Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
