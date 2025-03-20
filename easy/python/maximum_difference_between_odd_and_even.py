"""
You are given a string s consisting of lowercase English letters. Your task is to find the maximum difference between the frequency of two characters in the string such that:

One of the characters has an even frequency in the string.
The other character has an odd frequency in the string.
Return the maximum difference, calculated as the frequency of the character with an odd frequency minus the frequency of the character with an even frequency.
"""


class Solution(object):
    def maxDifference(self, s):
        array_letters = []
        array_times = []
        array_odd = []
        array_even = []
        for i in range(len(s)):
            if s[i] not in array_letters:
                array_letters.append(s[i])
                times = s.count(s[i])
                array_times.append(times)
            else:
                continue
        order_array = sorted(array_times)

        for number in order_array:
            if number % 2 != 0:
                array_odd.append(number)
            else:
                array_even.append(number)

        sorted_array_even = sorted(array_even)
        sorted_array_odd = sorted(array_odd)

        return sorted_array_odd[-1] - sorted_array_even[0]
