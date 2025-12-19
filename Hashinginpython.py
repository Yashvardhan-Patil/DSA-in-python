#In this example we will check how many time the element in m will come in element in n
n=[5,1,2,3,5,7,4,2,5,]
m=[4,2,8,7,2,5,6,3,1]

hash_list=[0,1,2,3,4,5,6,7,8]
num=hash_list
hash_list=[0]*9
for num in n:
    hash_list[num]+=1
for num in m:
    if num<1 or num>8:
        print(0)
    else:
        print(hash_list[num])

#character hashing
s="azyxyyzaaaa"
q=["a","a","y","z"]
hash_list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for ch in s:
    ascii_value=ord(ch)
    index=ascii_value-97
    hash_list[index]+=1
for ch in q:
    ascii_value=ord(ch)
    index=ascii_value-97
    print(hash_list[index])