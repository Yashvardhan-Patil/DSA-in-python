#brute force
class Solution(object):
    def singleNumber(self, nums):
        hash_map={}
        arr=[1,3,4,5,5,4,3]
        for nums in arr:
            hash_map[nums]=hash_map.get(nums,0)+1
        for key in hash_map:
            if hash_map[key]==1:
                return key
       

#Optimal solution
class Solution(object):
    def singleNumber(self, nums):
        ans=0
        for num in nums:
            ans=ans^num
        return ans
