"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/recover-binary-search-tree/description/
"""


class Solution(object):
    def recoverTree(self, root):
        self.first = self.second = self.prev = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node

            self.prev = node
            inorder(node.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
