/*
 * @lc app=leetcode id=107 lang=cpp
 *
 * [107] Binary Tree Level Order Traversal II
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void levelOrderBottom_helper(vector<TreeNode*> root_list, vector<vector<int>>& val_list){
        int n = root_list.size();
        if (n == 0){
            return;
        }
        vector<TreeNode*> next_level_list;
        vector<int> tmp_val;
        for(int i = 0; i < n; ++i){
            TreeNode* tmp = root_list[i];
            tmp_val.push_back(tmp->val);
            if(tmp->left){
                next_level_list.push_back(tmp->left);
            }
            if(tmp->right){
                next_level_list.push_back(tmp->right);
            }
        }
        levelOrderBottom_helper(next_level_list, val_list);
        val_list.push_back(tmp_val);
        return;

    }
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        if (!root){
            return {};
        }
        vector<vector<int>> res;
        levelOrderBottom_helper({root}, res);
        return res;
    }
};
// @lc code=end

