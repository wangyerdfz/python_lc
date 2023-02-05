#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def count_nodes_helper(root_):
            def left_depth(root_l):
                if root_l is None:
                    return 0
                return 1 + left_depth(root_l.left)
            def right_depth(root_r):
                if root_r is None:
                    return 0
                return 1 + right_depth(root_r.right)
            ld = left_depth(root_)
            rd = right_depth(root_)
            if ld == rd:
                return 2**ld - 1
            return 1 + count_nodes_helper(root_.left) + count_nodes_helper(root_.right)

        return count_nodes_helper(root)
# @lc code=end

