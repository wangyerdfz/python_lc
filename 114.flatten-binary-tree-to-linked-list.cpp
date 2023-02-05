/*
 * @lc app=leetcode id=114 lang=cpp
 *
 * [114] Flatten Binary Tree to Linked List
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
    void get_element(TreeNode *root, vector<TreeNode*>& res){
        if (root){
            res.push_back(root);
            get_element(root->left, res);
            get_element(root->right, res);
        }
    }
    void flatten(TreeNode* root) {
        if(!root){
            return;
        }
        vector<TreeNode*> res;
        get_element(root, res);
        TreeNode* fake_head = new TreeNode(1);
        TreeNode* cur = fake_head;
        for(int i = 0; i < res.size(); ++i){
            cur->left = nullptr;
            cur->right = res[i];
            cur = cur->right;
        }
        cur->left = nullptr;
        cur->right = nullptr;
    }
};
// @lc code=end

