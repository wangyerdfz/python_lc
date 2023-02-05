#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        tmp = dummy_head
        carry = 0
        while (l1 is not None) or (l2 is not None):
            sum_ = carry

            if l1 is not None:
                sum_ += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_ += l2.val 
                l2 = l2.next
            carry = sum_ // 10
            sum_ = sum_ % 10
            tmp.next = ListNode(sum_)
            tmp = tmp.next
        if carry > 0:
            tmp.next = ListNode(carry)
        return dummy_head.next




        # dummy_head = ListNode(0)
        # tmp = dummy_head
        # carry = 0
        # while (l1 is not None) & (l2 is not None):
        #     sum_ = l1.val + l2.val + carry
        #     if sum_ > 9:
        #         sum_ = sum_%10
        #         carry = 1
        #     else:
        #         carry = 0
        #     tmp.next = ListNode(sum_)
        #     tmp = tmp.next
        #     l1 = l1.next
        #     l2 = l2.next

        # if (l1 is None):
        #     while(l2 is not None):
        #         sum_ = l2.val + carry
        #         if sum_ > 9:
        #             sum_ = sum_%10
        #             carry = 1
        #         else:
        #             carry = 0
        #         tmp.next = ListNode(sum_)
        #         tmp = tmp.next
        #         l2 = l2.next
        #     if carry == 1:
        #         tmp.next = ListNode(1)
        # else:
        #     while(l1 is not None):
        #         sum_ = l1.val + carry
        #         if sum_ > 9:
        #             sum_ = sum_%10
        #             carry = 1
        #         else:
        #             carry = 0
        #         tmp.next = ListNode(sum_)
        #         tmp = tmp.next
        #         l1 = l1.next
        #     if carry == 1:
        #         tmp.next = ListNode(1)
        
        # return dummy_head.next

        # head = None
        # tmp = None
        # carry = 0
        # while (l1 is not None) or (l2 is not None):
        #     sum_ = carry
        #     if l1 is not None:
        #         sum_ = sum_ + l1.val
        #         l1 = l1.next
        #     if l2 is not None:
        #         sum_ = sum_ + l2.val
        #         l2 = l2.next
        #     carry = sum_//10
        #     sum_ = sum_%10

        #     node = ListNode(sum_)
        #     if tmp is None:
        #         tmp = node
        #         head = node
        #     else:
        #         tmp.next = node
        #         tmp = tmp.next

        # if carry :
        #     tmp.next = ListNode(carry)

        # return head

# @lc code=end

