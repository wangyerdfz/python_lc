#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (57.80%)
# Likes:    10105
# Dislikes: 271
# Total Accepted:    797.1K
# Total Submissions: 1.3M
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.
# 
# 
# Example 1:
# 
# 
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# 
# 
# Example 2:
# 
# 
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right






class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build_bin_tree(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            root_val = preorder[preorder_index]
            root_ = TreeNode(root_val)
            preorder_index += 1

            root_.left = build_bin_tree(left, inorder_map[root_val] - 1)
            root_.right = build_bin_tree(inorder_map[root_val] + 1, right)
            return root_

        preorder_index = 0
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        root = build_bin_tree(0, len(preorder) - 1)
        return root

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

#         def array_to_tree(left, right):
#             nonlocal preorder_index
#             # if there are no elements to construct the tree
#             if left > right: return None

#             # select the preorder_index element as the root and increment it
#             root_value = preorder[preorder_index]
#             root = TreeNode(root_value)


#             preorder_index += 1

#             # build left and right subtree
#             # excluding inorder_index_map[root_value] element because it's the root
#             root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
#             root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

#             return root

#         preorder_index = 0

#         # build a hashmap to store value -> its index relations
#         inorder_index_map = {}
#         for index, value in enumerate(inorder):
#             inorder_index_map[value] = index

#         return array_to_tree(0, len(preorder) - 1)
# @lc code=end

