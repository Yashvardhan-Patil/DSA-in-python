class solution:
    def checkbit(self,n,k):
       m=n | (1<<k)
       return m
        
n = int(input("Enter a number: "))
k = int(input("Enter bit position to check : "))

obj = solution()
result = obj.checkbit(n, k)
print(result)