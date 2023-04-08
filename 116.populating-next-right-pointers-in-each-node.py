#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        q = deque()
        q.append(root)
        while(len(q) > 0):
            prev = None
            size = len(q)
            while( size > 0):
                cur = q.popleft()
                cur.next = prev
                prev = cur
                if cur.right : q.append(cur.right)
                if cur.left : q.append(cur.left)
                size -= 1
        return root
# @lc code=end

