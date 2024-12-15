"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/sort-colors/description/
"""


class Solution(object):
    def sortColors(self, nums):
        count = [0, 0, 0]

        for num in nums:
            count[num] += 1

        ind = 0
        for i in range(3):
            for j in range(count[i]):
                nums[ind] = i
                ind += 1
        return nums