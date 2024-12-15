"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/replace-the-substring-for-balanced-string/description/
"""

from collections import Counter


class Solution(object):
    def balancedString(self, s):
        k = len(s)
        tgt = k // 4
        count = Counter(s)

        if all(val <= tgt for val in count.values()):
            return 0

        min_len = k
        left = 0
        for right in range(k):
            count[s[right]] -= 1
            while all(val <= tgt for val in count.values()):
                min_len = min(min_len, right - left + 1)
                count[s[left]] += 1
                left += 1

        return min_len