#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 
        tmp_root = TreeNode(1)
        cur_node = tmp_root

        def flatten_helper(root_):
            nonlocal cur_node
            if root_ is None:
                return
            cur_node.right = TreeNode(root_.val)
            cur_node = cur_node.right
            flatten_helper(root_.left)
            flatten_helper(root_.right)
            return
        flatten_helper(root)
        root.left = None
        root.right = tmp_root.right.right
        return
        
# @lc code=end

