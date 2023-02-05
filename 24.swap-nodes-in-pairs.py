#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake_head = ListNode(0)
        fake_head.next = head
        iter_head = fake_head
        while(iter_head.next and iter_head.next.next):
            tmp = iter_head.next
            tmp_end = tmp.next.next
            iter_head.next = tmp.next
            iter_head.next.next = tmp
            tmp.next = tmp_end
            iter_head = iter_head.next.next

        return fake_head.next
        
# @lc code=end

