import itertools
from memory_profiler import profile


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


def create_params(amount: int):
    names = ["Alice", "Bob", "Peter"]
    exp = [1, 2, 5, 10]
    sal = list(range(1, amount, 10))
    params = list(itertools.product(names, exp, sal))
    return params


@profile
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
