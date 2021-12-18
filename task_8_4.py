def val_checker(checker):
    def _val_checker(func):
        def wrapper(*args, **kwargs):
            if not all([checker(a) for a in args]):
                raise ValueError(f'wrong val: {[a for a in args if not checker(a)]}')
            return func(*args, **kwargs)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_something(x, y, z):
    return x ** 3 + y - z


if __name__ == '__main__':
    res = calc_something(5, -4, 5)
    print(res)
