#ascending order


# def fuc(n):
#     x = len(n)
#     for i in range(x):
#         min_index = i
#         for j in range(i + 1, x):
#             if n[j] < n[min_index]:
#                 min_index = j
#         # swap inside the outer loop
#         n[i], n[min_index] = n[min_index], n[i]
#     return n

# n = [1, 5, 7, 2, 3, 8]
# print(fuc(n))

#descending order
def func(nums):
    n=len(nums)
    for i in range(n):
        max_index=i
        for j in range(i+1,n):
            if nums[j]>nums[max_index]:
                max_index=j
        nums[i],nums[max_index]=nums[max_index],nums[i]
    return nums
nums=[1,2,3,4,5,6]
print(func(nums))


