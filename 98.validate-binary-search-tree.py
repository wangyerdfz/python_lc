#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right





class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # non local method
        prev_node = TreeNode(-2**31 - 2)

        def is_valid_bst_dup(root_):
            nonlocal prev_node
            if root_ is None:
                return True
            res_left = is_valid_bst_dup(root_.left)
            if prev_node.val >= root_.val:
                return False
            prev_node = root_
            res_right = is_valid_bst_dup(root_.right)
            return (res_left and res_right)

        return is_valid_bst_dup(root)

        # self.prev_node = TreeNode(-2**31 - 2)
        # def is_valid_bst_dup(root_):
        #     if root_ is None:
        #         return True
        #     res_left = is_valid_bst_dup(root_.left)
        #     if self.prev_node.val >= root_.val:
        #         return False
        #     self.prev_node = root_
        #     res_right = is_valid_bst_dup(root_.right)
        #     return (res_left and res_right)
        # return is_valid_bst_dup(root)



        # # alternative method:
        # def convert_to_list(root):
        #     if root is None:
        #         return []
        #     return convert_to_list(root.left) + [root.val] + convert_to_list(root.right)
        # ordered_list = convert_to_list(root)
        # for i in range(len(ordered_list) - 1 ):
        #     if ordered_list[i] >= ordered_list[i + 1]:
        #         return False
            
        # return True
        # def is_valid_BST_helper(root, min_ = None, max_ = None):
        #     if min_ is not None:
        #         if root.val <= min_:
        #             return False
        #     if max_ is not None:
        #         if root.val >= max_:
        #             return False
        #     if root.left is None and root.right is None:
        #         return True
        #     if root.left is None:
        #         # set up new min
        #         if min_ is None:
        #             right_min = root.val
        #         else:
        #             right_min = max(min_, root.val)
        #         return (root.val < root.right.val) and is_valid_BST_helper(root.right, right_min, max_)
        #     if root.right is None:
        #         if max_ is None:
        #             left_max = root.val
        #         else:
        #             left_max = min(root.val, max_)
        #         return (root.val > root.left.val) and is_valid_BST_helper(root.left, min_, left_max)
        #     if max_ is None:
        #         left_max = root.val
        #     else:
        #         left_max = min(root.val, max_) 
        #     if min_ is None:
        #         right_min = root.val
        #     else:
        #         right_min = max(min_, root.val)
            
        #     return (root.val > root.left.val) and (root.val < root.right.val) and is_valid_BST_helper(root.left, min_, left_max) and is_valid_BST_helper(root.right, right_min, max_)


        # return is_valid_BST_helper(root) 
                # return (root.val < root.right.val) and is_valid_BST_helper()
        # if root.left is None and root.right is None:
        #     return True
        # if root.left is None:
        #     return (root.val < root.right.val) and self.isValidBST(root.right)
        # if root.right is None:
        #     return (root.val > root.left.val) and self.isValidBST(root.left)
        # return (root.val < root.right.val) and (root.val > root.left.val) and self.isValidBST(root.left) and self.isValidBST(root.right)
# @lc code=end

