#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from functools import lru_cache


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def rob_helper(root):
            if root is None:
                return 0
            if root.left is None:
                left_val_rob = 0
                left_val_leave = 0
            else:
                left_val_rob = rob_helper(root.left.left) + rob_helper(root.left.right)
                left_val_leave = rob_helper(root.left)
            if root.right is None:
                right_val_rob = 0
                right_val_leave = 0
            else:
                right_val_rob = rob_helper(root.right.left) + rob_helper(root.right.right)
                right_val_leave = rob_helper(root.right)

            return max(left_val_rob + right_val_rob + root.val, left_val_leave + right_val_leave)

        return rob_helper(root)

# @lc code=end

