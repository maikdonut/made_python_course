def merge(seq_1,seq_2):
    return sorted(set(seq_1) & set(seq_2))

assert merge([1, 1, 2, 5, 7], [1, 1, 2, 3, 4, 7]) == [1, 2, 7]
assert merge([-2, -2, -2, -2], []) == []
assert merge([1, 1], [1, 1, 1, 1]) == [1]
assert merge([2, 4, 6, 8], [1, 3, 5, 7]) == []
assert merge([10, 20, 30], [10, 20, 30]) == [10, 20, 30]
assert merge([], []) == []

seq_1 = [int(x) for x in input().split()]
seq_2 = [int(x) for x in input().split()]
merge(seq_1,seq_2)
