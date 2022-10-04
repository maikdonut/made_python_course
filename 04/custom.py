"""Module providing function uniting elemens into tuple."""
from itertools import zip_longest


class CustomList(list):
    """
    A class inherited from list
    """

    def __init__(self, array):
        super().__init__(array)

    def check(self, array):
        """
        Check that object other is an instance of class CustomList
        """
        if isinstance(self, type(array)):
            return True
        raise TypeError("Can not make operations with different types")

    def calculation(self, array, other, sign):
        """
        Make sum and subtraction calculation
        """
        result = CustomList([])
        if self.check(other):
            [
                result.append((eval(f"{i} {sign} {j}")))
                for i, j in zip_longest(array, other, fillvalue=0)
            ]
            return result

    def __add__(self, other):
        return self.calculation(self, other, "+")

    def __radd__(self, other):
        return self.calculation(other, self, "+")

    def __sub__(self, other):
        return self.calculation(self, other, "-")

    def __rsub__(self, other):
        return self.calculation(other, self, "-")

    def __eq__(self, other):
        if self.check(other):
            return sum(self) == sum(other)

    def __ne__(self, other):
        if self.check(other):
            return sum(self) != sum(other)

    def __lt__(self, other):
        if self.check(other):
            return sum(self) < sum(other)

    def __le__(self, other):
        if self.check(other):
            return sum(self) <= sum(other)

    def __gt__(self, other):
        if self.check(other):
            return sum(self) > sum(other)

    def __ge__(self, other):
        if self.check(other):
            return sum(self) >= sum(other)

    def __str__(self):
        return "Array: %s\nSum of elements: %s" % (
            "[" + ", ".join(map(str, self)) + "]",
            sum(self),
        )
