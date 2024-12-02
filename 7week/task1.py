"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/permutation-in-string/description/
"""

from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False

        c_s1 = Counter(s1)
        c_wdw = Counter(s2[:len1])

        if c_s1 == c_wdw:
            return True

        for i in range(len1, len2):
            c_wdw[s2[i]] += 1
            c_wdw[s2[i - len1]] -= 1
            if c_wdw[s2[i - len1]] == 0:
                del c_wdw[s2[i - len1]]
            if c_s1 == c_wdw:
                return True

        return False