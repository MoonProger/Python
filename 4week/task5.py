"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/merge-intervals/description/
"""


class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged