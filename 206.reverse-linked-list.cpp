/*
 * @lc app=leetcode id=206 lang=cpp
 *
 * [206] Reverse Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(!head){
            return head;
        }
        ListNode* pre = new ListNode(0);
        ListNode* cur = head;
        pre->next = head;
        while(cur->next && cur){
            ListNode* tmp = pre->next;
            pre->next = cur->next;
            cur->next = cur->next ->next;
            pre->next->next = tmp;

        }
        return pre->next;
    }
};
// @lc code=end

