#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur = head
        list_ = []
        while(cur is not None):
            list_.append(cur.val)
            cur = cur.next
        fake_head = ListNode(0)
        cur = fake_head
        left_ = []
        right_ = []
        for val_ in list_:
            if val_ < x:
                left_.append(val_)
            else:
                right_.append(val_)
        
        for val_ in left_ + right_:
            cur.next = ListNode(val_)
            cur = cur.next
        return fake_head.next
# @lc code=end

