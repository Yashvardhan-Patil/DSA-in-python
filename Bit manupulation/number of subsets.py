class Solution(object):
    def subsets(self, nums):
        n=len(nums)
        m=2**n
        result=[]
        for num in range(0,m):
            list=[]
            for i in range(n):
                if num & (1<<i)!=0:
                    list.append(nums[i])
            result.append(list)
        return result

obj=Solution()
print(obj.subsets(nums=[1,2,4,5]))
