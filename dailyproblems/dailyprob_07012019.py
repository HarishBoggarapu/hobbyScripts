# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

# Solution 1:
# 1) get all combinations (length of 2) of the list
# 2) check each combination if sum of the combination equals K value

from itertools import combinations

numList = [1, 2, 4, 5, 6]
Kvalue = 10


def checkKsumEquals(numList, Kvalue):
    Kequals = [True for comb in combinations(numList, 2) if (sum(comb) == Kvalue)]
    print(Kequals[0])
    # for i in list(comb):
    # print(sum(i) == Kvalue)


checkKsumEquals(numList, Kvalue)
