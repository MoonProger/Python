"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q or (not root):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left:
            return left

        return right
