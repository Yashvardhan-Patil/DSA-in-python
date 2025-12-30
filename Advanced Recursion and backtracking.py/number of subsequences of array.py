def fun(index, subset):
    nums = [1, 2, 3, 4, 5]

    if index >= len(nums):
        result.append(subset.copy())
        return

    subset.append(nums[index])
    fun(index + 1, subset)

    subset.pop()
    fun(index + 1, subset)


result = []      # list to store all subsets
fun(0, [])

# printing subsets
for s in result:
    print(s)
