"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/unique-binary-search-trees/description/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def numTrees(self, n):
        K = [0] * (n + 1)
        K[0] = 1
        K[1] = 1
        # Catalan
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                K[nodes] += K[root - 1] * K[nodes - root]

        return K[n]

