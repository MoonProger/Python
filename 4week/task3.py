"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/spiral-matrix/description/
"""


class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        result = []
        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while up <= down and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[up][i])
            up += 1

            for i in range(up, down + 1):
                result.append(matrix[i][right])
            right -= 1

            if up <= down:
                for i in range(right, left - 1, -1):
                    result.append(matrix[down][i])
                down -= 1

            if left <= right:
                for i in range(down, up - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result