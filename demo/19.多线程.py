"""
线程：threading.Thread()  耗时操作
    状态：
        新建 就绪 运行 阻塞 结束

    线程是可以共享全局变量的

GIL 全局 解释器 锁
注意：
    python底层只要用线程默认加锁
    线程运算量大的话  就会自动释放锁
    所以运算量大的话建议用进程
建议：
    线程：耗时操作，爬虫
    进程：计算密集型
"""
import threading
from multiprocessing import Queue
from time import sleep


def download(q):
    images = ['aa.jpg', 'bb.jpg', 'cc.jpg', 'dd.jpg']
    for image in images:
        sleep(.2)
        q.put(image)
        print('{}下载成功！'.format(image))


if __name__ == '__main__':
    q = Queue()
    t = threading.Thread(target=download, args=(q,))
    t.start()
