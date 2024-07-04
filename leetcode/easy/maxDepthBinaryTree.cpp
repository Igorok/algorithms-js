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
/*
maxDepthBinaryTree.cpp
*/



class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;

        int depth = 1;

        int leftDepth = root->left ? this->maxDepth(root->left) : 0;
        int rightDepth = root->right ? this->maxDepth(root->right) : 0;

        return depth + std::max(leftDepth, rightDepth);
    }
};
