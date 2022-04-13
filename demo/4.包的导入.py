"""
一个包中可以放多个模块
项目 ---》 包 ---》 模块 ---》 类 函数 变量

_init___.py   初始化文件  只要导入包  默认执行init文件

    from 包.模块 import 类
    from 包.模块 import *
        使用*导入的时候，如果不想被访问执行可以时候 __all__  = [允许被看到的类或者变量]
        if __name__ == '__main__':
            pass       
"""

# 使用包中模块中的User类
from user.models import User

u = User('xiaohei', '20')
u.__str__()
