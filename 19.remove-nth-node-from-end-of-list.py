#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # step 1 figure out the length:
        len_ = 1
        temp_iter = head
        while(temp_iter.next is not None):
            temp_iter = temp_iter.next
            len_ += 1
        if len_ == n:
            return head.next
        counter = 0
        fwd_iter = head
        while(counter < len_ - n - 1):
            fwd_iter = fwd_iter.next
            counter += 1

        fwd_iter.next = fwd_iter.next.next
        return head


        
# @lc code=end

