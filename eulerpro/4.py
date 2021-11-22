'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

ans = []

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

for a in range(100, 1000):
    for b in range(100, 1000):
        if par(str(a * b)) == 1:
            ans.append(a * b)

print(ans)
print(max(ans))