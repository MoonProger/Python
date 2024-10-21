"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/valid-sudoku/description/
"""


class Solution(object):
    def isValidSudoku(self, board):
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

                n = int(num) - 1

                if rows[i][n] == 1:
                    return False
                rows[i][n] = 1

                if cols[j][n] == 1:
                    return False
                cols[j][n] = 1

                box_ind = (i // 3) * 3 + (j // 3)
                if boxes[box_ind][n] == 1:
                    return False
                boxes[box_ind][n] = 1

        return True


