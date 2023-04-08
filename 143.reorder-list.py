#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return 
        q = deque()
        cur = head
        while(cur is not None):
            q.append(cur)
            cur = cur.next
        fake_head = ListNode(0)
        cur = fake_head
        while(len(q) > 0):
            cur.next = q.popleft()
            cur = cur.next
            if (len(q) > 0):
                cur.next = q.pop()
                cur = cur.next

        cur.next = None
        return

        
        
# @lc code=end

