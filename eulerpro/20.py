'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
a = 1
for b in range(1,101):
    a *= b
fak = []
for c in str(a):
    fak.append(int(c))
print(a)
print(fak)
print(sum(fak))