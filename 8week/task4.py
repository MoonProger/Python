"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/new-21-game/description/
"""


class Solution(object):
    def new21Game(self, n, k, maxPts):
        if k == 0 or n >= k + maxPts:
            return 1.0
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        win_sum = 1.0
        res = 0.0

        for p in range(1, n + 1):
            dp[p] = win_sum / maxPts
            if p < k:
                win_sum += dp[p]
            else:
                res += dp[p]
            if p >= maxPts:
                win_sum -= dp[p - maxPts]

        return res

