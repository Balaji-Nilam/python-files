s=input()
count=0
new_str=""
for i in s:
    if i=="-":
        count+=1
for i in s:
    if i!="-":
        new_str+=i
print("-"*count+new_str)
