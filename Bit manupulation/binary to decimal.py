def D(x:str)->int:
    decimal=0
    power=0
    index=len(x)-1
    while index>=0:
        y=int(x[index])*(2**power)
        decimal+=y
        index-=1
        power+=1
    return decimal
print(D("1101"))