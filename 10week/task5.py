"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
"""


class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None

        cur = head
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next

        def build_bst(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = build_bst(nums[:mid])
            root.right = build_bst(nums[mid + 1:])
            return root

        return build_bst(nums)