nums=[[0,2,7],[7,3,5],[8,9,2]]
rows=len(nums)
columns=len(nums[0])
for i in range(0,rows):
    for j in range(0,columns):
        if i>=j:
            print(nums[i][j],end=" ")
    print()
