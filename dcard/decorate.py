import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*arg, **kwarg):
        time_start = time.time()
        value = func(*arg, **kwarg)
        time_end = time.time()
        time_spend = time_end - time_start

        print(f"[{func.__name__}] function cost time: {time_spend}")

        return value

    return wrapper