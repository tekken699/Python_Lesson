from functools import wraps

def val_cheker(l_func):
    def _val_cheker(func):

        @wraps(func)
        def wraper(num):
            if l_func(num):
                print(l_func(num))
            else:
                raise ValueError(f'wrong wal {num}')
        return wraper

    return _val_cheker

@val_cheker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

try:
    a = calc_cube(-5)
    print(help(calc_cube))
except (ValueError, TypeError) as err:
    print(err)