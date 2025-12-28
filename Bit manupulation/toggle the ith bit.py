class solution:
    def checkbit(self,n,k):
        n ^ (1<<k)
        return n
            
n = int(input("Enter a number: "))
k = int(input("Enter bit position to check : "))

obj = solution()
result = obj.checkbit(n, k)