'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

class Chain:
    def __init__(self, value):
        self.value = value
        self.listOfChain = []
        
    def makeChain(self):
        self.value2 = self.value
        while self.value2 != 1:
            self.listOfChain.append(self.value2)
            if  self.value2 % 2 == 1:
                self.value2 = (self.value2 * 3) + 1
            else:
                self.value2 = self.value2 / 2

    def countChain(self):
        return len(self.listOfChain)

allChain = [[],[]] #[[value], [countChain]]
for a in range(1, 1000000):
    c = Chain(a)
    c.makeChain()
    allChain[0].append(c.value)
    allChain[1].append(c.countChain())

maxChain = max(allChain[1])
indexAnswer = allChain[1].index(maxChain)
Answer = allChain[0][indexAnswer]

print(Answer)


