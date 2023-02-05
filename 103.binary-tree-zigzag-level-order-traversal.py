#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is  None:
            return []
        result_list = []
        odd_level = True

        def solve(k):
            nonlocal odd_level
            if not k:
                return 
            ans, new_k = [], []
            if odd_level:
                for item in k:
                    ans.append(item.val)
            else:
                for item in reversed(k):
                    ans.append(item.val)
            for item in k:
                if item.left is not None:
                    new_k.append(item.left)
                if item.right is not None:
                    new_k.append(item.right)
            result_list.append(ans)
            odd_level = not odd_level
            solve(new_k)

        solve([root])
        return result_list


        # if root is  None:
        #     return []
        # result_list = []
        # # odd_level = True

        # def solve(k, level):
        #     if not k:
        #         return 
        #     ans, new_k = [], []
        #     if level%2 == 1:
        #         for item in k:
        #             ans.append(item.val)
        #     else:
        #         for item in reversed(k):
        #             ans.append(item.val)
        #     for item in k:
        #         if item.left is not None:
        #             new_k.append(item.left)
        #         if item.right is not None:
        #             new_k.append(item.right)
        #     result_list.append(ans)
        #     # odd_level = not odd_level
        #     solve(new_k, level + 1)

        # solve([root], 1)
        # return result_list
# @lc code=end

