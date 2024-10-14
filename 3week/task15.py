"""
leetcode.com/problem-list/array
url: https://leetcode.com/problems/maximum-subarray/description/
"""

class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        cur_sum = nums[0]

        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum