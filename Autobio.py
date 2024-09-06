def bio(num):
    for i in range(len(num)):
        if int(num[i])>len(num):
            return False
        if int(num[i])!=num.count(str(i)):
            return False
    return True

    
num='6210001000'
if(bio(num)):
    print("bio")
else:
    print("no")
