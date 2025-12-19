class Solution(object):
    def rearrangeArray(self, nums):
        n=len(nums)
        result=[0]*n
        posi,neg=0,1
        for i in range(n):
            if nums[i]>=0:
                result[posi]=nums[i]
                posi+=2
            else:
                result[neg]=nums[i]
                neg+=2
        return result
nums=[5,4,7,-8,-9,-7]
obj=Solution()
print(obj.rearrangeArray(nums))

        
        