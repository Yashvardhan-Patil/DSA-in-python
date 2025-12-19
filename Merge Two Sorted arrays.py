def fun(nums1,nums2):
    nums1.sort()
    nums2.sort()
    n=len(nums1)
    m=len(nums2)
    i=0
    j=0
    merge=[]
    while i<n and j<m:
        if nums1[i]<=nums2[j]:
            if len(merge)==0 or merge[-1]!=nums1[i]:
               merge.append(nums1[i])
            i+=1
        else:
            if len(merge)==0 or merge[-1]!=nums2[j]:
                merge.append(nums2[j])
            j+=1
    while i<n:
        if len(merge)==0 or merge[-1]!=nums1[i]:
               merge.append(nums1[i])
        i+=1
        
    while j<m:
         if len(merge)==0 or merge[-1]!=nums2[j]:
                merge.append(nums2[j])
         j+=1
    return merge
nums1=[1,3,4,5,7,8,3]
nums2=[1,5,7,8,1,2,1,0]
print(fun(nums1,nums2))

                
