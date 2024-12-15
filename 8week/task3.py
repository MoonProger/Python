"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
"""

from collections import Counter


class Solution(object):
    def numberOfSubstrings(self, s):
        count = Counter()
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while all(count[c] > 0 for c in 'abc'):
                res += len(s) - right
                count[s[left]] -= 1
                left += 1

        return res