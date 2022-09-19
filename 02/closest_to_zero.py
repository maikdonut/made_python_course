def closest_zero(nums): 
    assert len(nums) != 0, "Empty list"
    pos_nums = [abs(i) for i in nums]
    close = min(pos_nums)
    result = []
    for i in range(len(nums)):
        if pos_nums[i] == close:
            result.append(nums[i])
    return result
        
assert closest_zero([1, -1, 1, -1, 1, 1]) == [1, -1, 1, -1, 1, 1]
assert closest_zero([2, 2, -5, 9, 3, -2]) == [2, 2, -2]
assert closest_zero([-5, -10, -2, -5]) == [-2]
assert closest_zero([4, 1, 3, 2, 5]) == [1]
assert closest_zero([6, -1, 1, 3, 0]) == [0]

nums = [int(x) for x in input().split()]
closest_zero(nums)
