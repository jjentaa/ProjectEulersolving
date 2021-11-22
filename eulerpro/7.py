'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

prime = []

i = 1
while len(prime) < 10001:
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
        prime.append(i)
    i += 1 

print(prime[10000])