import time
from collections import deque


def mean(k):
    d = deque(maxlen=k)

    def wrap(function):
        def called(*args):
            start_time = time.perf_counter_ns()
            d.append(time.perf_counter_ns() - start_time)
            res = sum([x for x in d if isinstance(x, int)])/len(d)
            return res
        return called
    return wrap


@mean(10)
def foo(arg1):
    pass

@mean(2)
def boo(arg1):
    pass

for _ in range(100):
    print(foo("Walter"))
