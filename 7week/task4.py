"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices/description/
"""

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        if len(nums) < 3:
            return 0

        cur_len = 0
        count = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                cur_len += 1
                count += cur_len
            else:
                cur_len = 0

        return count