import functools
from colorama import init, Fore, Style

init(autoreset=True)  # Automatically reset color after each print

def color(color_code, color_name='color'):
    def wrapper(func):
        @functools.wraps(func)
        def runner(*args, **kwargs):
            print(color_code + f'Changing to {color_name}...')
            func(*args, **kwargs)
            print(Style.RESET_ALL, end='')  # Ensure reset if autoreset is off
        return runner
    return wrapper

@color(color_code=Fore.RED, color_name='red')
def greeter():
    print('Hello, world!!')
    print('Just saying hi again')

greeter()