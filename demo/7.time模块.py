"""
重点记住：
    time()  时间戳
    sleep() 倒计时
    strftime('格式') 年-月-日 时：分：秒
    localtime()  返回元组年月日时分秒

    datetime模块：
        time 时间
        date 日期
        datetime 日期时间
        timedelta 时间差 timedelta(days='',weeks=''.....)
"""

import time
import datetime  # 底层还是time封装的

t = time.time()  # 获取当前时间的时间戳
# time.sleep(3) # 延迟3秒
print(t)
s = time.ctime(t)  # 将时间戳转成字符串
print(s)
# 将时间戳转成元组
t = time.localtime(t)  # 获取年月日时分秒
print(t)
print(t.tm_year)
print(t.tm_mon)
print(t.tm_mday)

tt = time.strftime("%Y-%m-%d" + " %H:%M:%S")  # 字符串年月日时分秒 2022-01-13 16:24:11
print(tt)

print(datetime.date.today())  # 2022-01-13
