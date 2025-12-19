#Method1
nums=[12,5,4,6,7,7,12,5]
hash_map=dict()
n=len(nums)
for i in range(0,n):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1
print(hash_map)

#Method2

nums=[12,5,4,6,7,7,12,5]
hash_map=dict()
for i in range (0,len(nums)):
    if nums[i] in hash_map:
        hash_map[nums[i]]+=1
    else:
        hash_map[nums[i]]=1
print(hash_map)
