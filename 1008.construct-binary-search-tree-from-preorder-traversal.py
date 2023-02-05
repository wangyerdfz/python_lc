#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        if n <= 0:
            return None
        top_val = preorder[0]
        top = TreeNode(top_val)
        i = 1
        while(i < n):
            if preorder[i] > top_val:
                break
            i += 1
        top.left = self.bstFromPreorder(preorder[1:i])
        top.right = self.bstFromPreorder(preorder[i:])
        return top

        
# @lc code=end

