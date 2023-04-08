#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        if (root.left is None) and (root.right is None):
            if root.val == targetSum:
                return [[root.val]]
            return []
        
        left_list = self.pathSum(root.left, targetSum - root.val) 
        right_list = self.pathSum(root.right, targetSum - root.val) 
        total_list = left_list + right_list
        return [[root.val] + x for x in total_list]

# @lc code=end

