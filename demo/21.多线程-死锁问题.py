"""
死锁：
    死锁产生是因为开发过程中，在线程间共享多个资源的时候，
    如果两个线程分别占有一部分资源，并且同时等待对方的资源，就会造成死锁

    尽管死锁很少发生，一旦发生就会造成应用的停止响应，程序不会做任何事情

避免死锁：
    1、重构代码
    2、使用timeout参数解决  在 lock.acquire(timeout=5)  # 阻塞   会自动释放锁
"""
