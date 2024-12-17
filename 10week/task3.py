"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        cur = root

        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur
