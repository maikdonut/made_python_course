def split_nums(nums):
    if len(nums) == 0:
        return 'List is empty'
    odd = []
    even = []
    for i in nums:
        if i == 0:
            continue
        elif i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(odd) == 0 and len(even) == 0:
        return 'List of zeros is given'
    return (even,odd)

assert split_nums([4, 2, 3, 1]) == ([4, 2], [3, 1])
assert split_nums([2, 3, -1, 10, 0, 20, 31, -5]) == ([2, 10, 20], [3, -1, 31, -5])
assert split_nums([2, 4, 8, 8, 10]) == ([2, 4, 8, 8, 10], [])
assert split_nums([1, 1, 1]) == ([], [1, 1, 1])
assert split_nums([]) == 'List is empty'
assert split_nums([0, 0]) == 'List of zeros is given'

nums = [int(x) for x in input().split()]
split_nums(nums)
