def fun(nums, target):
    first = -1
    last = -1

    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i

    return [first, last]

nums = [1,2,3,3,3,4,5]
print(fun(nums, 3))
