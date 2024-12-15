"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/max-consecutive-ones-iii/description/
"""


class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        max_len = 0
        zero_c = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_c += 1

            while zero_c > k:
                if nums[left] == 0:
                    zero_c -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len