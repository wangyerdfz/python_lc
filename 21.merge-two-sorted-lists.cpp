/*
 * @lc app=leetcode id=21 lang=cpp
 *
 * [21] Merge Two Sorted Lists
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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* head = new ListNode(0);
        ListNode* cur = head;
        while( list1 || list2){
            if (not list1){
                cur->next = list2;
                return head->next;
            }
            if (not list2){
                cur->next = list1;
                return head->next;
            }
            if (list1->val < list2->val){
                cur->next = list1;
                list1 = list1->next;
                cur = cur->next;
            }
            else{
                cur->next = list2;
                list2 = list2->next;
                cur = cur->next;
            }
        }
        return head->next;
    }
};
// @lc code=end

