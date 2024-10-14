"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/generate-parentheses/description/
"""


class Solution(object):
    def generateParenthesis(self, n):
        result = []

        cur_stack = [""]
        opened = [0]
        closed = [0]

        while cur_stack:
            cur = cur_stack.pop()
            open_count = opened.pop()
            close_count = closed.pop()

            if len(cur) == 2 * n:
                result.append(cur)
                continue


            if open_count < n:
                cur_stack.append(cur + "(")
                opened.append(open_count + 1)
                closed.append(close_count)

            if close_count < open_count:
                cur_stack.append(cur + ")")
                opened.append(open_count)
                closed.append(close_count + 1)

        return result