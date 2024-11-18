"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-size-subarray-sum/description/
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        cur_sum = 0
        min_len = 10000000000

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1

        if min_len != 10000000000:
            return min_len
        else:
            return 0
