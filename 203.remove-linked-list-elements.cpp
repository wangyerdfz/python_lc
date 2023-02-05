/*
 * @lc app=leetcode id=203 lang=cpp
 *
 * [203] Remove Linked List Elements
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
    ListNode* removeElements(ListNode* head, int val) {
        if(!head){
            return head;
        }
        ListNode* new_head = new ListNode(INT_MAX);
        new_head->next = head;
        ListNode* prev = new_head;
        ListNode* cur = new_head->next;
        while(cur){
            if(cur->val == val){
                prev->next = cur->next;
                cur =cur->next;
            }
            else{
                cur = cur->next;
                prev = prev->next;
            }
        }
        return new_head->next;
    }
};
// @lc code=end

