nums = [int(x) for x in input().split()]
assert len(nums) != 0, 'List is empty'
odd = []
even = []
for i in nums:
    if i == 0:
        continue
    elif i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
assert len(odd) != 0 and len(even) != 0, 'List of zeros is given'
print('Odd numbers:',*odd)
print('Even numbers:',*even)
