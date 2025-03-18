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