"""
单例模式：开发模式
单例是一种设计模式，应用该模式的类只会生成一个实例
通过 object__new__()
"""


class func1:
    pass

p = func1()
p1 = func1()
print(p)
print(p)

