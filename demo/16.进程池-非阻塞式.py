"""
Pool.apply_async()


非阻塞式: （进程达到复用）
    全部添加到队列中，立刻返回，并没有等待其他的其他的进程执行完毕，但是回调函数是等待任务完毕后才会执行

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
        pool.apply_async(task, args=(task1,), callback=call_back) # 创建异步进程池

    pool.close()
    pool.join() #

    for c in container:
        print(c)
