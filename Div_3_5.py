m=int(input())
n=int(input())
sum=0
for i in range(m,n):
    if i%3==0 and i%5==0:
        sum+=i
print(sum)
