class solution:
    def get(self,a,b):
        a=a^b
        b=a^b
        a=a^b
        return [a,b]
obj=solution()
print(obj.get(4,5))