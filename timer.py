### Task 5.5

# Using magic method `__call__` implement a decorator which can accept parameters.
# It can do anything you want until it's implemented as a class, overrides the `__call__`
# method and is parametrised.

# # Example:
# ```python
# class Timer:
# """My beautiful timer implementation.
# Counts the time that function takes to run.
# If parameter is provided it will sleep for a setted amount of seconds.
# It's 0 by default."""
#     ...

 # >>> @Timer()
#      def factorial(n):
#      return functools.reduce(lambda x, y: x*y, [1] + list(range(1, n + 1)))

# "The func took 3.123283386230469e-05 seconds with 0 seconds sleep."
# 1405006117752879898543142606244511569936384000000000


# >>> @Timer(10)
#      def factorial(n):
#      return functools.reduce(lambda x, y: x*y, [1] + list(range(1, n + 1)))

# "The func took 10.008108139038086 seconds with 10 seconds sleep."
# 1405006117752879898543142606244511569936384000000000

import time
import functools

class Timer:
    def __init__(self, time_to_wait=0):
        self.wait = time_to_wait

    def __call__(self, function):
        def inner(*args, **kwargs):
            time.sleep(self.wait)
            start_time = time.time()
            res = function(*args, **kwargs)
            return res, time.time() - start_time, self.wait
        return inner

@Timer(2)
def factorial(n):
    return functools.reduce(lambda x, y: x*y, [1] + list(range(1, n + 1)))

if __name__=='__main__':
    res, time_run, time_sleep = factorial(2000)
    print(f'The func took {time_run} seconds with {time_sleep} seconds sleep. ')
