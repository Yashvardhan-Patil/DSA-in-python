def sub(index,total,subset):
    nums=[4,5,9]
    target=9
    if total==target:
        result.append(subset.copy())
        return
    elif total>target:
        return
    if index>=len(nums):
        return
    subset.append(nums[index])
    total+=nums[index]
    sub(index+1,total,subset)

    e=subset.pop()
    total=total-e
    sub(index+1,total,subset)

result=[]
sub(0,0,[])

for s in result:
    print(s)
    