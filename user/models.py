__all__ = ['User']

version = '1.1.0'


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print(self.name, self.age)


if __name__ == '__main__':  # 只有本模块执行的时候才会打印，
    print('-----user-----')
