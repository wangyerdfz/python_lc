#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import numpy as np


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.fake_head = ListNode(0)
        self.fake_head.next = head
        len_ = 0
        tmp = head
        while(tmp):
            len_ += 1
            tmp = tmp.next
        self.len_ = len_

    def getRandom(self) -> int:
        k = np.random.randint(1, self.len_+1)
        tmp = self.fake_head
        while(k>0):
            tmp = tmp.next
            k-=1
        return tmp.val


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

