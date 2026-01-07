from typing import List
class Solution:
    def solve(self,k,n,last,total,subset,result):
        if total==n and len(subset)==k:
            result.append(subset.copy())
            return
        if total>n or len(subset)>k:
            return

        for i in range(last,10):
            sum=total+i
            subset.append(i)
            self.solve(k,n,i+1,sum,subset,result)
            subset.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        self.solve(k,n,1,0,[],result)
        return result
        