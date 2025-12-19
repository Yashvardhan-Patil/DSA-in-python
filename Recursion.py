#Function calling itself again and again
#Q1 print yash 4 times

#1 head recursion: first the funct() will be called and then the print statement
count=0
def funct():
    global count #This tells that use count variable that is outside the function
    if count==4:
        return 
    print("Yash")
    count+=1
    
    funct()
funct()

#2 Tail recursion(opposite to HR)
count=0
def funct():
    global count
    if count==5:
        return
    count+=1
    funct()
    print("Yash")
funct()