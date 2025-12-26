def B(num:int)->str:
    result=""
    while num>0:
        
        if num%2==1:
            result+="1"
        else:
            result+="0"
        num=num//2
    result=result[::-1]
    return result
print(B(13))