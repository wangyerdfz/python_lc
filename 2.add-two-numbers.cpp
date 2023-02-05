/*
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head {new ListNode {0}};
        ListNode* cur {head};
        int offset {0};
        while(l1 || l2 || offset){
            if(l1){
                offset += l1->val;
                l1 = l1->next;
            }
            if(l2){
                offset += l2->val;
                l2 = l2->next;
            }
            cur->next = new ListNode {offset % 10};
            cur = cur->next;
            offset = offset / 10;
        }

        return head->next;


        // ListNode* head { new ListNode {0}};
        // ListNode* cur {head};
        // int offset {0};
        // while( l1 || l2){
        //     int num_one {0};
        //     int num_two {0};
        //     if (l1){
        //         num_one = l1->val;
        //         l1 = l1->next;
        //     }
        //     if (l2){
        //         num_two = l2->val;
        //         l2 = l2->next;
        //     }
        //     int sum_ = num_one + num_two + offset;
        //     offset = sum_ / 10;
        //     cur -> next = new ListNode {sum_ % 10};
        //     cur = cur->next;

        // }
        // if (offset > 0){
        //     cur->next = new ListNode {offset};
        // }
        // return head->next;
    



        
//         ListNode* head = new ListNode(0);
//         ListNode* cur = head;
//         int extra = 0;
//         while( l1 || l2 || extra){
//             if (l1){
//                 extra += l1->val;
//                 l1 = l1->next;
//             }
//             if (l2){
//                 extra += l2->val;
//                 l2 = l2->next;
//             }
//             cur->next = new ListNode(extra % 10);
//             extra = extra / 10;
//             cur = cur->next;
//         }
//         return head->next;
    }
};
// @lc code=end

