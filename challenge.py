import time


def finish_date(func):
    def internal_func(*args, **kwargs):
        func(*args, **kwargs)
        print(f'The function {func.__name__} finished at {time.strftime("%d/%m/%Y - %H:%M:%S", time.gmtime())}')
    return internal_func


@finish_date
def palindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


@finish_date
def long_function():
    for _ in range(1000000):
        pass


def run():
    palindrome('Ana')
    long_function()


if __name__ == '__main__':
    run()
