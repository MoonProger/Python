"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
"""

class Solution(object):
    def findLength(self, nums1, nums2):
        n, m = len(nums1), len(nums2)

        dp = []
        for i in range(n + 1):
            dp.append([0] * (m + 1))

        max_len = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])

        return max_len