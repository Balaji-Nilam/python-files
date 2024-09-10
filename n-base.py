n='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num1=int(input())
num2=int(input())
s=''
while num2>0:
    res=num2%num1
    s=n[res]+s
    num2=num2//num1
print(s)
