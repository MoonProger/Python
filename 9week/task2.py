"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
"""

from collections import deque


class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []

        q = deque([root]) #q - queue
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

            res.insert(0, lvl_nodes)

        return res