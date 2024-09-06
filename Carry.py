num1=int(input())
num2=int(input())
count=0
carry=0
while num1>0 or num2>0:
    res1=num1%10
    res2=num2%10
    num1=num1//10
    num2=num2//10
    res=res1+res2+carry
    if res>9:
        count+=1
        carry=1
    else:
        carry=0
print(count)
        
