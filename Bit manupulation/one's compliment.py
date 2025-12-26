def one(num:int)->str:
    result=""
    while num>0:
        if num%2==1:
            result+="0"
        else:
            result+="1"
        num=num//2
    result=result[::-1]
    return result
print(one(13))