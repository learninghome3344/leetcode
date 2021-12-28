/*
 * @lc app=leetcode.cn id=101 lang=cpp
 *
 * [101] 对称二叉树
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

#include <iostream>
#include <queue>
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        std::queue<TreeNode*> q;
        q.push(root->left);
        q.push(root->right);
        while (!q.empty()) {
            TreeNode* p1 = q.front(); q.pop();
            TreeNode* p2 = q.front(); q.pop();
            if (!p1 && !p2) continue;
            if (!p1 || !p2 || p1->val != p2->val) return false;
            q.push(p1->left);
            q.push(p2->right);
            q.push(p1->right);
            q.push(p2->left);
        }
        return true;
    }


    // bool isSymmetric(TreeNode* root) {
    //     if (!root) return false;
    //     return helper(root->left, root->right);
    // }

    // bool helper(TreeNode *p, TreeNode *q) {
    //     if (!p && !q) return true;
    //     if (!p || !q) return false;
    //     return (p->val == q->val) && helper(p->left, q->right) && helper(p->right, q->left);
    // }
};
// @lc code=end

