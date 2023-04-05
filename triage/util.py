from halo import Halo
import functools

def spinning(text='Loading'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            spinner = Halo(text=text, spinner="dots")
            spinner.start()
            try:
                result = func(*args, **kwargs)
            finally:
                spinner.stop()
            return result
        return wrapper
    return decorator