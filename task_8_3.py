def type_logger(func):
    def logged(*args, **kwargs):
        print(func.__name__ + '(', end='')
        print(', '.join(f'{a}: {type(a)}' for a in args), end='')
        print(')')
    return logged


@type_logger
def calc_something(x,y,z):
    return x ** 3 + y + z


if __name__ == '__main__':
    calc_something(5,4,5)


