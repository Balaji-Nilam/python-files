m = 0
max_val = 0
for i in range(int(input()),int(input())):
    count = 0
    n = i
    while n % 2 == 0:
        n //= 2
        count += 1
    if count > max_val:
        max_val = count
        m = i
print(m)
