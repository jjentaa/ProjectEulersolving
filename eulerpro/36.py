'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
'''

def par(a):
    c = 0
    for b in range(len(a)//2):
        if a[b] != a[(len(a)-b-1)]:
            r = 0
            break
        c += 1

    if c == (len(a)//2):
        r = 1
    
    return r

ans = []
for e in range(1, 1000000):
    d = bin(e)[2:]
    if par(str(e)) == 1 and par(str(d)) == 1:
        ans.append(e)
print(ans)
print(sum(ans))