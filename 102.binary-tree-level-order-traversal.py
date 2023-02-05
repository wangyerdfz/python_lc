#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return_list = []
        def solve(k):
            if not k:
                return
            ans, new_k = [], []
            for item in k:
                ans.append(item.val)
                if item.left is not None:
                    new_k.append(item.left)
                if item.right is not None:
                    new_k.append(item.right)
            return_list.append(ans)
            solve(new_k)

        if root is None:
            return []
        solve([root])
        return return_list


                    
# @lc code=end

