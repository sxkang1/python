"""
进程间通信：Queue

"""
from multiprocessing import Process, Queue
from time import sleep


def download(q):
    images = ['aa.jpg', 'bb.jpg', 'cc.jpg', 'dd.jpg']
    for image in images:
        sleep(.2)
        q.put(image)
        print('{}下载成功！'.format(image))


def getfile(q):
    while True:
        try:
            file = q.get(timeout=3)
            print('{}保存成功！'.format(file))
        except:
            print('全部保存成功！')
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))

    p1.start()
    p1.join()  # 不加join，就是下载一个保存一个
    p2.start()
    p2.join()
