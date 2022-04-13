"""
. 任意字符串（\n）
^ 开头
$ 结尾
[] 范围 [abc] [a-z] [a-z*&$]
() 一组  ---> group(1)

正则预定义：
    \s 空白 空格
    \b  边界
    \d 数字
    \w word [0-9a-zA-Z]

    \S 非空格
    \D 非数字

量词：
    * >=0
    + >=1
    ? 0,1
    {m}  =m
    {m,} >=m
    {m,n} >=m <=n


re模块：
    match(pattern,str)
    search(pattern,str)
    findall(pattern,str)
    sub(pattern正则表达式，‘新内容’，string) 替换
    split(pattern,str) 切割 ---》[]

# 默认是贪婪的，如果想将贪婪模式转换成非贪婪  加？
"""
import re

import requests

msg = 'a3b ah4 e5l fdsfs'
result = re.search('[a-z][0-9][a-z]', msg)  # search 匹配到就不会继续往下找了
print(result)

result = re.findall('[a-z][0-9][a-z]', msg)  # findall 匹配整个字符串 一直到结尾
print(result)

# match是从头开始匹配，【1-9】是首位不能是0，【0-9】余下的必须是数字
# {4,10}是最少五位  最多是一位 首位是【1-9】表示了
# $ 是匹配到最后 ^是必须从头开始匹配  因为我们用了match所以不用^，也是从头开始匹配

qq = '12308'
result = re.match('[1-9][0-9]{4,10}$', qq)
print(result)

# 不是以4,7结尾的手机号码（11位）

phone = '15194424485'
result = re.match(r'1\d{9}[0-35-689]$', phone)
print(result)

# 起名方式：<(?P<name1>正则)> (.+) </(?P=name1)>
# .+ 表示一位以上
msg = '<html><h1>abc</h1></html>'
result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>', msg)
print(result)
print(result.group(1))
print(result.group(2))
print(result.group(3))

path = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2F44cbe44ee3cce9f39c3823b48d324c1bf15330e77c1f2-9xYsnm_fw658&amp;refer=http%3A%2F%2Fhbimg.b0.upaiyun.com&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=jpeg?sec=1644743988&amp;t=b714d31b04894b83d49bf941c75ca56b" width="398.17435897436" height="708" style="top: 0px; left: 66px; width: 355.432px; height: 632px; cursor: pointer;" log-rightclick="p=5.102" title="点击查看图片来源">'
result = re.match(r'<img src="(.*?)"', path)
print(result.group(1))

path = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_match%2F0%2F11863118161%2F0.jpg&refer=http%3A%2F%2Finews.gtimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1644744345&t=79f935abfb82b3ec835218f78b300d4b'
result = requests.get(path)
with open('aa.jpg', 'wb') as wstream:
    # print(result.content)
    wstream.write(result.content)
