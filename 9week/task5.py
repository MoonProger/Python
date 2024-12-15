"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        q = deque([root])
        res = []
        left_right = True
        while q:
            lvl_size = len(q)
            lvl_nodes = deque()

            for i in range(lvl_size):
                node = q.popleft()

                if left_right:
                    lvl_nodes.append(node.val)
                else:
                    lvl_nodes.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(list(lvl_nodes))
            left_right = not left_right

        return res