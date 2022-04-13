"""
循环的导入： 大型的python项目中，需要很多py文件，由于架构不当，可能会出现模块之间相互调用
    避免产生循环导入：
        1、重新架构
        2、将导入的语句放在函数里面
        3、把导入语句放到模块的最后
    A模块：
        def test:
            func()
     B模块：
        def func:
            test()
"""