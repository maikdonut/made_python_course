from custom import CustomList


assert CustomList([10, 20]) - CustomList([30, 20, 10, 0]) == CustomList([-20, 0, -10, 0])
assert CustomList([2, 4, 6]) + CustomList([1, 3]) == CustomList([3, 7, 6])
assert [5] - CustomList([1, 3, 5]) == CustomList([4, -3, -5])
assert CustomList([1, 3, 5]) + [2, 4] == CustomList([3, 7, 5])
assert CustomList([2, 4, 6]) < CustomList([100])
assert CustomList([1, 2, 3, 4]) == [10]
assert CustomList([10, 20, 30]) >= CustomList([60])
