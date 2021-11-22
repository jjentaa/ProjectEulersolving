'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
first = 0
second = 0
for a in range(1,101):
    first += a ** 2
    second += a
second = second ** 2

print(second - first)