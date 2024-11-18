"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/longest-consecutive-sequence/description/
"""


class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        max_count = 0
        length = 0

        for i in nums:
            if i - 1 not in num_set:
                cur_count = 0
                while i + cur_count in num_set:
                    cur_count += 1
                max_count = max(max_count, cur_count)

        return max_count


