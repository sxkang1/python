def print_func(par):
    print('Hello,', par)


if __name__ == '__main__': # 只有在此文件执行时候再回调用  被当做模块引入不会去执行
    print(__name__)  # 在本模块叫__main__   被其他模块调用的话  叫做模块名 support
    print_func('oo')
