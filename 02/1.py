def closest_zero(nums): 
    nums = list(sorted(set(nums)))
    assert len(nums) != 0, "Empty list"
    neg = [i for i in nums if i < 0]
    pos = nums[len(neg):]
    
    if len(neg) == 0:
        return [pos[0]]
    elif len(pos) == 0:
        return [neg[-1]]
    else:
        if abs(neg[-1]) == pos[0]:
            return [neg[-1], pos[0]]
        elif abs(neg[-1]) > pos[0]:
            return [pos[0]]
        else:
            return [neg[-1]]
        
assert closest_zero([-5, 9, 6, -8]) == [-5]
assert closest_zero([1, 2, -5, -1]) == [-1, 1]
assert closest_zero([-5, -10, -2, -5]) == [-2]
assert closest_zero([4, 1, 3, 2, 5]) == [1]
assert closest_zero([6, -1, 1, 3, 0]) == [0]

nums = [int(x) for x in input().split()]
closest_zero(nums)