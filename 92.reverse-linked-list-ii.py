#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # flatten the linked list
        if head is None:
            return head
        list_ = []
        cur = head
        while(cur is not None):
            list_.append(cur.val)
            cur = cur.next
        left_ = list_[:left-1]
        right_ = list_[right:]
        mid_ = list(reversed(list_[left-1:right]))
        fake_head = ListNode(0)
        cur = fake_head
        for val_ in left_ + mid_ + right_:
            cur.next = ListNode(val_)
            cur = cur.next

        return fake_head.next
# @lc code=end

