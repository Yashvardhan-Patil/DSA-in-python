nums=[[0,2],[7,3],[8,9]]
rows=len(nums)
columns=len(nums[0])
rsult=[[0]*rows for _ in range(columns)]
for i in range(rows):
    for j in range(columns):
        rsult[j][i]=nums[i][j]
        print(rsult[j][i],end=" ")
    print()