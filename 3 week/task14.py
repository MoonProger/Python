"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/permutations/description/
"""


class Solution(object):
    def permute(self, nums):
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        res = []

        for i in range(len(nums)):
            current_num = nums[i]
            remaining_nums = nums[:i] + nums[i + 1:]
            for p in self.permute(remaining_nums):
                res.append([current_num] + p)

        return res