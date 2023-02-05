#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_trees_helper(start: int , end: int):
            if end < start:
                return [None]
            return_list = []
            for i in range(start, end + 1):

                left_list = generate_trees_helper(start, i - 1)
                right_list = generate_trees_helper(i + 1, end)
                for left_tree in left_list:
                    for right_tree in right_list:
                        top = TreeNode(i)
                        top.left = left_tree
                        top.right = right_tree
                        return_list.append(top)
            return return_list


        if n == 0:
            return []
        return generate_trees_helper(1, n)

        
# @lc code=end

