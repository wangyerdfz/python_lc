#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k_count = 0
        val_ = -1000000
        def kth_smallest_helper(root_, k_):
            nonlocal k_count
            nonlocal val_
            if root_ is None:
                return None
            kth_smallest_helper(root_.left, k_)
            k_count += 1
            if k_count == k_:
                val_ = root_.val
                return None
            kth_smallest_helper(root_.right, k_)
            return None
        if root is None:
            return 0
        kth_smallest_helper(root, k)
        return val_
# @lc code=end

