"""
协程：微线程 (第三方 gevent 遇到IO耗时操作，自动切换 底层是封装greenlet，)
    进程 > 线程 > 协程

协程晋级：生成器 ---> greenlet ---> gevent
gevent 使用的时候一般是和猴子补丁一起使用  解释器3.9以后就不需要了
协程：高效利用CPU  别让CPU闲着
使用场景：
    耗时操作的时候使用：网络下载(爬虫)，网络请求
    IO操作：(文件读写)
"""
from time import sleep

import gevent
# from gevent import monkey
#
# monkey.patch_all()


def a():
    for i in range(5):
        print('A---->', i)
        sleep(.5)  # 模拟阻塞


def b():
    for i in range(5):
        print('B---->', i)

        sleep(.2)  # 模拟阻塞


def c():
    for i in range(5):
        print('C---->', i)

        sleep(.3)  # 模拟阻塞


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()
