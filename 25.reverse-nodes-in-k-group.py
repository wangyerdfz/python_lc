#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1:
            return head
        val_list = []
        tmp = head
        while(tmp):
            val_list.append(tmp.val)
            tmp = tmp.next

        n = len(val_list)
        
        i = 0
        while(i * k + k  <= n):
            left = i*k
            right = i*k + k-1
            while(left < right):
                val_list[left], val_list[right] = val_list[right], val_list[left]
                left += 1
                right -= 1

            i += 1
        
        head = ListNode(0)
        cur = head
        for i in val_list:
            cur.next = ListNode(i)
            cur = cur.next

        return head.next


# @lc code=end

