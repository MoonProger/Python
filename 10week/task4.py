"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
"""


class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or (not postorder):
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)

        root_ind = inorder.index(root_val)
        root.right = self.buildTree(inorder[root_ind + 1:], postorder)
        root.left = self.buildTree(inorder[:root_ind], postorder)

        return root