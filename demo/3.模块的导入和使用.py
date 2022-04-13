"""
1、自定义模块
2、使用系统的一些模块

文件与文件的导入

导入模块：
    1、import 模块名
        模块名.变量 模块名.函数 模块.类
    2、from 模块名 import 变量 | 函数 | 类

    3、from 模块名 import *
       该模块中所有的内容
       但是如果想限制获取的内容，可以在模块中使用__all__ = [使用了*可以访问到内容]
"""

# import support
# support.print_func()

from support import *
print_func('小康')
