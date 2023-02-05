/*
 * @lc app=leetcode id=61 lang=cpp
 *
 * [61] Rotate List
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
    ListNode* rotateRight(ListNode* head, int k) {
        int len = 1;
        if (not head){
            return head;
        }
        ListNode* end = head;

        while(end->next){
            end = end->next;
            len++;
        }
        if (len == 0){
            return head;
        }
        while(k >= len){
            k = k%len;
        }
        if (k == 0){
            return head;
        }
        ListNode* cur = head;
        for (int i = 0;i < len - k - 1; ++i){
            cur = cur->next;
        }
        end->next = head;
        ListNode* res = cur->next;
        cur->next = nullptr;
        return res;
        // return head;

    }
};
// @lc code=end

