"""
协程：微线程 (第三方 greenlet 人工切换任务)
    进程 > 线程 > 协程

协程晋级：生成器 ---> greenlet ---> gevent

协程：高效利用CPU  别让CPU闲着
使用场景：
    耗时操作的时候使用：网络下载(爬虫)，网络请求
    IO操作：(文件读写)
"""
from time import sleep

from greenlet import greenlet


def a():
    for i in range(5):
        print('A---->', i)

        gb.switch()  # 切换b任务
        sleep(.5)  # 模拟阻塞


def b():
    for i in range(5):
        print('B---->', i)
        gc.switch()  # 切换c任务
        sleep(.5)  # 模拟阻塞


def c():
    for i in range(5):
        print('C---->', i)
        ga.switch()  # 切换a任务
        sleep(.5)  # 模拟阻塞


if __name__ == '__main__':
    ga = greenlet(a)
    gb = greenlet(b)
    gc = greenlet(c)

    ga.switch()
