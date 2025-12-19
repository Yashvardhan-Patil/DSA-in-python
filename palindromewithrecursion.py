def func(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
         return False
    return func(s,left+1,right-1)
s="niti"
print(func(s,0,3))

print("Second Type:")
def func(s,left,right):
    if s[left]!=s[right]:
        return False
    if s[left]==s[right]:
        return True
    func(s,left+1,right-1)

s="MOM"
print(func(s,0,2))
    
#Using while loop
print("Third tye:")
s="ABCCBA"
n=len(str(s))
left=0
right=n-1
while left<right:
    
    if s[left]!=s[right]:
        print(False)
    left+=1
    right-=1
print(True)
