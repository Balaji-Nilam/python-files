arr=list(map(int,input().split()))
even=arr[0]
odd=arr[1]
for i in range(len(arr)):
    if i%2==0 and even<arr[i]:#largest < symbol
        even=arr[i]
    elif i%2!=0 and odd>arr[i]:#smallest > symbol
        odd=arr[i]
print(even+odd)
