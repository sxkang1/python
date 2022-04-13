import re

msg = '娜扎热巴佟丽娅'

pattern = re.compile('佟丽娅')
result = pattern.match(msg)  # None
print(result)

s = '佟丽娅迪丽热巴'
result = re.match('热巴', s)  # match是从头开始匹配，开始没匹配上就返回None
print(result)

result = re.search('热巴', s)  # search是逐步向后搜索
print(result)
print(result.span())  # 获取位置
print(result.group())  # 提取匹配内容部分
