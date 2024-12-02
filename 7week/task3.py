"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
"""

from collections import Counter

class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0

        frq = Counter(s)
        for c, count in frq.items():
            if count < k:
                subs = s.split(c)
                lens = []
                for substr in subs:
                    lens.append(self.longestSubstring(substr, k))
                return max(lens)

        return len(s)
