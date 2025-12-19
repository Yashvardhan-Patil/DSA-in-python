def fun(nums):
    r=len(nums)
    c=len(nums[0])
    rowtrack=[0 for _ in range(r)]
    columntrack=[0 for _ in range(c)]
    for i in range(r):
        for j in range(c):
            if nums[i][j]==0:
                rowtrack[i]=-1
                columntrack[j]=-1
    for i in range(r):
        for j in range(c):
            if rowtrack[i]==-1 or columntrack[j]==-1:
                nums[i][j]=0
        
    return nums
    
nums=[[0,4,5],[1,2,3],[3,0,2]]
print(fun(nums))



    