/*
 * @lc app=leetcode.cn id=110 lang=cpp
 *
 * [110] 平衡二叉树
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
    bool m_balanced = true;

    bool isBalanced(TreeNode* root) {
        maxDepth(root);
        return m_balanced;
    }

    int maxDepth(TreeNode* root) {
        if (!root || !m_balanced) return -1;
        int l = maxDepth(root->left);
        int r = maxDepth(root->right);
        if (abs(l - r) > 1) {
            m_balanced = false;
            return -1;
        }
        return 1 + max(l, r);
    }
};
// @lc code=end

