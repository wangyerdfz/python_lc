#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_ = -10000000
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_helper(root)
        return self.max_
    

    def max_helper(self, root):
        if root is None:
            return 0
        l = max(self.max_helper(root.left), 0)
        r = max(self.max_helper(root.right), 0)
        self.max_ = max(self.max_, l + r + root.val)
        return max(l, r) + root.val
# @lc code=end

