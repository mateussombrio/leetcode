'''
You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:

Replace each even number with 0.
Replace each odd numbers with 1.
Sort the modified array in non-decreasing order.
Return the resulting array after performing these operations.
'''
class Solution(object):
    def transformArray(self, nums):
        anotherNums = []
        for num in nums:
            if num % 2 == 0:
                num = 0
                anotherNums.append(num)
            else:
                num = 1
                anotherNums.append(num)
        return sorted(anotherNums)