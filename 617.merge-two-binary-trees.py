#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        ret_root = TreeNode(root1.val + root2.val)
        ret_root.left = self.mergeTrees(root1.left, root2.left)
        ret_root.right = self.mergeTrees(root1.right, root2.right)
        return ret_root
# @lc code=end

