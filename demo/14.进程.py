"""
格式：
    process = Process(target=函数,name=进程的名字,args=给函数传递的参数)

    process.start()  启动进程并执行任务
    process.run()   只是执行了任务但是没有启动进程
    process.terminate()  终止进程

"""
# 进程的创建
import os
import multiprocessing
from time import sleep


def task1(i, name):
    while True:
        sleep(1)
        print('任务1----', os.getpid(), '-----------', os.getppid(), name)


def task2(i, name):
    while True:
        sleep(1)
        print('任务2----', os.getpid(), '-----------', os.getppid(), name)


number = 1
if __name__ == '__main__':

    p1 = multiprocessing.Process(target=task1, name='任务1', args=(1, 'task1'))
    p1.start()
    print('---------name1:', p1.name)
    p2 = multiprocessing.Process(target=task2, name='任务2', args=(2, 'task2'))
    print('---------name2:', p2.name)
    p2.start()
    while True:
        number += 1
        sleep(.1)
        print('------number:',number)
        if number == 100:
            p1.terminate()
            p2.terminate()
            break

print('******************')

