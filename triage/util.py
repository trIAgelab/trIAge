import functools
import os

from halo import Halo


def get_secret(key):
    """ Get a secret from the secrets directory."""
    secret_file = os.path.join("../secrets", f"{key}.txt")
    with open(secret_file, 'r') as f:
        secret = f.readline().strip()
    return secret

def spinning(text='Loading'):
    """ A decorator to show a spinner while a function is running."""
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