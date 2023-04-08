#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        straighten_list = []
        ind_list = []
        cur = head
        straighten_list.append(cur.val)
        ind_list = [0]
        cur = cur.next
        while(cur):
            if straighten_list[-1] == cur.val:
                ind_list[-1] = 1
            else:
                straighten_list.append(cur.val)
                ind_list.append(0)
            cur = cur.next
        new_head = ListNode(0)
        cur = new_head
        for idx, val in enumerate(straighten_list):
            if ind_list[idx] == 0:
                cur.next = ListNode(val)
                cur = cur.next
        
        return new_head.next

        



# @lc code=end

