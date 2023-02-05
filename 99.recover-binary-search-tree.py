#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        # non local version
        prev_element = TreeNode(-2**31 -2)
        first_element = None
        second_element = None
        
        def mark_two_elements(root_):
            nonlocal prev_element
            nonlocal first_element
            nonlocal second_element
            if root_ is None:
                return None
            mark_two_elements(root_.left)
            if (first_element is None) and (prev_element.val >= root_.val):
                first_element = prev_element
            if (first_element is not None) and (prev_element.val >= root_.val):
                second_element = root_
            prev_element = root_
            mark_two_elements(root_.right)
            return None

        mark_two_elements(root)
        tmp = first_element.val
        first_element.val = second_element.val
        second_element.val = tmp

        return None

        # self.prev_element = TreeNode(-2**31 -1)
        # self.first_element = None
        # self.second_element = None
        # def recover_tree_helper(root):
        #     if root is None:
        #         return None
        #     recover_tree_helper(root.left)
        #     if (self.first_element is None) and (self.prev_element.val >= root.val):
        #         self.first_element = self.prev_element
        #     if (self.first_element is not None) and (self.prev_element.val >= root.val):
        #         self.second_element = root
        #     self.prev_element = root
        #     recover_tree_helper(root.right)
        #     return None
        # recover_tree_helper(root)
        # tmp = self.first_element.val
        # self.first_element.val = self.second_element.val
        # self.second_element.val = tmp
        # return root
        
# @lc code=end

