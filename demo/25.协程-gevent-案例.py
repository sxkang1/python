import gevent
import requests


def download(path):
    response = requests.get(path)
    content = response.text
    print('下载了%s的数据，长度为%d' % (path, len(content)))


if __name__ == '__main__':
    url = ['http://www.baidu.com', 'http://www.taobao.com', 'http://www.jd.com', 'http://www.163.com']
    for i in url:
        g = gevent.spawn(download, i)
        g.join()
