"""
Pool.apply()

阻塞式:
    添加一个任务，执行一个任务，如果一个任务不结束，另外一个任务就进不来

进程池：
    pool = Pool(max) 创建进程池对象
    pool.apply()    阻塞的
    pool.apply_async()  非阻塞的

    pool.close()
    pool.join() 让主进程让步
"""
import os
from multiprocessing import Pool
import time
from random import random


def task(task_name):
    print('开始做任务了', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random() * 2)
    end = time.time()
    return '完成任务：{}！用时：{}，进程ID：{}'.format(task_name, (end - start), os.getpid())


container = []


def call_back(n):
    container.append(n)


if __name__ == '__main__':
    pool = Pool(5)

    tasks = ['吃饭', '睡觉', '打豆豆', '洗衣服', '看电视', '看电影', '逛街']
    for task1 in tasks:
        pool.apply(task, args=(task1,)) # 创建异步进程池

    pool.close()
    pool.join() #

    for c in container:
        print(c)
