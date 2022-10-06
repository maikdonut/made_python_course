import time
from collections import deque


def mean(k):
    d = deque(maxlen=k)

    def wrap(function):
        def called(*args):
            start_time = time.perf_counter_ns()
            function_res = function(*args)
            d.append(time.perf_counter_ns() - start_time)
            res_time = sum([x for x in d if isinstance(x, int)])/len(d)
            print(res_time)
            return function_res
        return called
    return wrap


@mean(5)
def func(a, b):
    return a + b

for i, j in zip(range(10**5, 10**5 + 10), range(10**5, 10**5 + 10)):
    func(i, j)
