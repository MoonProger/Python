"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        q = deque([root])
        res = []
        while q:
            lvl_nodes = []
            lvl_size = len(q)

            for i in range(lvl_size):
                node = q.popleft()
                lvl_nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(lvl_nodes)

        return res