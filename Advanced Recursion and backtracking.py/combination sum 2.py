class Solution:
    def backtrack(self,index,total,subset,nums,result):
       
        n=len(nums)
        
        if total==0:
            result.append(subset.copy())
            return
        if total<0:
            return
        for i in range(index,n):
            if i>index and nums[i]==nums[i-1]:
                continue
            subset.append(nums[i])
            sum=total-nums[i]
            self.backtrack(i+1,sum,subset,nums,result)
            subset.pop()


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        self.backtrack(0,target,[],candidates,result)
        return result
        