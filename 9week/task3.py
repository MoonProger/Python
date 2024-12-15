"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/validate-binary-search-tree/description/
"""


class Solution(object):
    def isValidBST(self, root):
        def check(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False

            return (check(node.left, min_val, node.val) and
                    check(node.right, node.val, max_val))

        return check(root, float('-inf'), float('inf'))