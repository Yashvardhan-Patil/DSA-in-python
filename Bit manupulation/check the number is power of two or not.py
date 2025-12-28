class solution:
    def checkbit(self,n,k):
        if n & n-1==0:
            return True
        return False
            
n = int(input("Enter a number: "))
k = int(input("Enter bit position to check : "))

obj = solution()
result = obj.checkbit(n, k)