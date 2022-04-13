"""
python允许多继承
    def 子类(父类1，父类2，父类3):
        pass
经典类：从左至右，广度优先（对于python）
新式类：
查看搜索顺序：对象.__mro__
多态：
    通过 isinstance(obj,类) 判断多态是否是一个类型，
"""

class test1:
    def func(self):
        print('test1 func')

class test2:
    def func(self):
        print('test2 func')


class test3(test1,test2):
    pass
p = test3()
p.func()

