import weakref
import itertools
from memory_profiler import profile


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


@profile
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
    empl_params = list(
        itertools.product(names, exp, sal)
    )  # 12000000 emploees
    run(empl_params)
