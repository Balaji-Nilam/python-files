s=input()
char1=input()#python default data type string
char2=input()#mundhu int,str ani m pettakapothe default str thisukuntadhi
new_str=''
for i in s:
    if i==char1:
        new_str+=char2
    elif i==char2:
        new_str+=char1
    else:
        new_str+=i
print(new_str)
