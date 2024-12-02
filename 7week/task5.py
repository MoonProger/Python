"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-repeating-character-replacement/description/
"""

from collections import Counter

class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        max_len = 0
        max_cnt = 0
        count = Counter()

        for right in range(len(s)):
            count[s[right]] += 1
            max_cnt = max(max_cnt, count[s[right]])

            while (right - left + 1) - max_cnt > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len