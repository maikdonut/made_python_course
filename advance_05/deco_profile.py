import itertools
import cProfile
import pstats


class Employee:
    def __init__(self, name: str, experience: int, salary: int):
        self.name = name
        self.experience = experience
        self.salary = salary


class SlotEmployee:
    __slots__ = ("name", "experience", "salary")

    def __init__(self, name: str, experience: int, salary: int):
        self.name = name
        self.experience = experience
        self.salary = salary


class WeakRefEmployee:
    __slots__ = ("name", "experience", "salary", "__weakref__")

    def __init__(self, name, experience, salary):
        self.name = name
        self.experience = experience
        self.salary = salary


class ProfileDeco:
    def __init__(self, func):
        self.func = func
        self.profiler = cProfile.Profile()
        self.stats = None

    def __call__(self, *args, **kwargs):
        result = self.profiler.runcall(self.func, *args, **kwargs)
        self.stats = pstats.Stats(self.profiler)
        return result

    def print_stats(self):
        self.stats.print_stats()


def create_params(amount: int):
    names = ["Alice", "Bob", "Peter"]
    exp = [1, 2, 5, 10]
    sal = list(range(1, amount, 10))
    params = list(itertools.product(names, exp, sal))
    return params


@ProfileDeco
def run(params):
    lst_a = [Employee(*i) for i in params]
    lst_slot = [SlotEmployee(*i) for i in params]
    lst_weak = [WeakRefEmployee(*i) for i in params]

    del lst_a
    del lst_slot
    del lst_weak


if __name__ == "__main__":
    N = 100_000
    empl_params = create_params(N)  # 120000 employes
    run(empl_params)
    run.print_stats()
