/*
 * @lc app=leetcode id=257 lang=cpp
 *
 * [257] Binary Tree Paths
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
    void binaryTreePaths_helper(TreeNode* root, vector<string>& res){
        // will not encounter root = nullptr case unless its the first node
        if(!root){
            return;
        }
        if(!root->left && !root->right){
            res.push_back(to_string(root->val));
            return;
        }
        int pre_size = res.size();
        if(root->left){
            binaryTreePaths_helper(root->left, res);
        }
        if(root->right){
            binaryTreePaths_helper(root->right, res);
        }
        for(int i = pre_size; i < res.size() ; ++i){
            res[i] = to_string(root->val) + "->" + res[i];
        }
        return ;


    }
    vector<string> binaryTreePaths(TreeNode* root) {
        if (!root){
            return {};
        }
        vector<string> s;
        binaryTreePaths_helper(root, s);
        return s;

    }
};
// @lc code=end

