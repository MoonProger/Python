"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        if len(p) > len(s):
            return res

        p_count = [0] * 26
        window = [0] * 26

        for char in p:
            p_count[ord(char) - ord('a')] += 1

        for i in range(len(s)):
            window[ord(s[i]) - ord('a')] += 1

            if i >= len(p):
                window[ord(s[i - len(p)]) - ord('a')] -= 1

            if window == p_count:
                res.append(i - len(p) + 1)

        return res
