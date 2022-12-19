import weakref
import itertools
import cProfile
import pstats
import io


class Employee:
    def __init__(self, name:str, experience:int, salary:int):
        self.name = name
        self.experience = experience
        self.salary = salary


class SlotEmployee:
    __slots__ = ("name", "experience", "salary")

    def __init__(self, name:str, experience:int, salary:int):
        self.name = name
        self.experience = experience
        self.salary = salary


def profileit(name):
    def inner(func):
        def wrapper(*args, **kwargs):
            prof = cProfile.Profile()
            retval = prof.runcall(func, *args, **kwargs)
            prof.dump_stats(name)
            return retval

        return wrapper

    return inner


@profileit("profile_for_func")
def run(params):
    lst_a = [Employee(*i) for i in params]
    lst_slot = [SlotEmployee(*i) for i in params]
    lst_weak = [weakref.ref(obj) for obj in lst_a]

    del lst_a
    del lst_slot
    del lst_weak


if __name__ == "__main__":
    N = 10_000_000
    names = ["Alice", "Bob", "Peter"]
    exp = [1, 2, 5, 10]
    sal = list(range(1, N, 10))
    empl_params = list(itertools.product(names, exp, sal))  # 12000000 emploees
    run(empl_params)
    s = io.StringIO()
    pr = pstats.Stats("profile_for_func")
    pr.print_stats()
    print(s.getvalue())
