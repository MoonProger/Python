"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/subarray-product-less-than-k/description/
"""


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        prod = 1
        left = 0
        count = 0
        for right in range(len(nums)):
            prod *= nums[right]

            while left <= right and prod >= k:
                prod //= nums[left]
                left += 1
            count += right - left + 1

        return count
