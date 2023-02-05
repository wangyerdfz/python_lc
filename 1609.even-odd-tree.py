#
# @lc app=leetcode id=1609 lang=python3
#
# [1609] Even Odd Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def is_even_odd_tree(node_list, level):
            if not node_list:
                return True
            if level%2 == 1: # odd level
                return_list = []
                prev_val = -1000000000
                for node_ in node_list:
                    if node_.val %2 != 1:
                        return False
                    if node_.val <= prev_val:
                        return False
                    if node_.left is not None:
                        return_list.append(node_.left)
                    if node_.right is not None:
                        return_list.append(node_.right)
                    prev_val = node_.val
            else:
                return_list = []
                prev_val = 1000000000
                for node_ in node_list:
                    if node_.val %2 != 0:
                        return False
                    if node_.val >= prev_val:
                        return False
                    if node_.left is not None:
                        return_list.append(node_.left)
                    if node_.right is not None:
                        return_list.append(node_.right)
                    prev_val = node_.val
            return is_even_odd_tree(return_list, level + 1)


        if root is None:
            return True
        return is_even_odd_tree([root], 1)
            
            
# @lc code=end

