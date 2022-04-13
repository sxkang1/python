import random

r = random.random()  # 0~1之间的随机数
print(r)
r = random.randrange(1, 10, 2)  # randrange(start,stop,step)
print(r)
r = random.randint(1, 10) #随机产生1~10  包含10
print(r)

list = ['a', 'b', 'c', 'd']
# r = random.choice(list)  # 随机产生一个字符串
# print(r)

# r = random.shuffle(list)
# print(r)
