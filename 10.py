s = 0
i = 1
while i < 2000000:
    j = 2
    if i%2 == 0 and i != 2:
        pass
    if i == 1:
        i+=1
    while j<=i//j:
        if i%j==0:
            break
        j+=1
    if j > i//j:
        s += i
    i += 1 

print(s)