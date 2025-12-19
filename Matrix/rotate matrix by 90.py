def fun(matrix):
    r=len(matrix)
    c=len(matrix[0])
    for i in range(0,r-1):
        for j in range(i+1,c):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(r):
        for j in range(c):
            matrix[i].reverse()
            print(matrix[i][j],end=" ")
        print()
matrix=[[0,2,3],[2,3,4],[5,4,8]]
print(fun(matrix))