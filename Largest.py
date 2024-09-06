num=list(map(int,input().split()))
lar=num[0]
index=0
for i in range(1,len(num)):
    if num[i]>lar:
        lar=num[i]
        index=i
print(lar,index)

#print(max(num),num.index(max(num)))
