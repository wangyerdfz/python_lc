/*
 * @lc app=leetcode id=110 lang=cpp
 *
 * [110] Balanced Binary Tree
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
    bool public_balanced = true;
    int max_depth(TreeNode* root){
        if (not root){
            return 0;
        }
        return max(max_depth(root->left), max_depth(root->right)) + 1;
    }
    bool isBalanced(TreeNode* root) {
        if (root){
            bool left_balanced = isBalanced(root->left);
            int left_depth = max_depth(root->left);
            int right_depth = max_depth(root->right);
            if (left_depth > right_depth + 1 || right_depth > left_depth + 1){
                return false;
            }
            bool right_balanced = isBalanced(root->right);
            return left_balanced&&right_balanced;
        }
        return true;
    }
};
// @lc code=end

