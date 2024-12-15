"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/zigzag-conversion/description/
"""

class Solution(object):
    def convert(self, s, num_rows):
        if num_rows == 1 or num_rows >= len(s):
            return s

        rows = [''] * num_rows

        cur_row = 0
        down = False

        for char in s:
            rows[cur_row] += char

            if cur_row == 0 or cur_row == num_rows - 1:
                down = not down

            if down:
                cur_row += 1
            else:
                cur_row -= 1

        return ''.join(rows)