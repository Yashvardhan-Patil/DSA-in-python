def fun(nums):
    ans=[]
    n=len(nums)
    nums.sort()
    target=8
    for i in range(n):
        if i>00 and nums[i]==nums[i-1]:
            continue
        for j in range(n):
            if j>i+1 and nums[i]==nums[i-1]:
                continue
       
        k=j+1
        l=n-1
        while k<l:
            total_sum=nums[i]+nums[j]+nums[k]+nums[l]
            if total_sum==target:
                temp=[nums[i],nums[j],nums[k],nums[l]]
                ans.append(temp)
                k+=1
                l-=1
                while k<l and nums[k]==nums[k-1]:
                    k+=1
                while k<l and nums[l]==nums[l+1]:
                    l-=1
            elif total_sum<target:
                k+=1
            else:
                i-=1
    return ans
nums=[1,2,2,3,2,2,2,2]
            