nums=[[0,5,7],[7,8,9],[1,2,3]]
rows=len(nums)
column=len(nums[0])
for i in range(0,rows):
    for j in range(0,column):
        if i<=j:
            print(nums[i][j],end=" ")
    print()
       