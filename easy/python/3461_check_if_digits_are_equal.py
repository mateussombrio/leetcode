"""
You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits:

- For each pair of consecutive digits in s, starting from the first digit, calculate a new digit as the sum of the two digits modulo 10.
- Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed.

Return true if the final two digits in s are the same; otherwise, return false.
"""


class Solution(object):
    def hasSameDigits(self, s):
        converted_s = []
        for number in s:
            converted_s.append(int(number))

        for j in range(len(s) - 2):
            for i in range(len(converted_s) - 1):
                sum = (converted_s[i] + converted_s[i + 1]) % 10
                converted_s[i] = sum
            converted_s.pop()
        return converted_s[0] == converted_s[1]