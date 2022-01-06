/*
 * @lc app=leetcode.cn id=61 lang=cpp
 *
 * [61] 旋转链表
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
        if (!head || k == 0) return head;
        int len = 1;
        ListNode* p = head;
        while (p->next) {
            p = p->next;
            ++len;
        }
        int move = len - k % len;
        p->next = head;
        for (int i = 0; i < move; ++i) {
            p = p->next;
        }
        ListNode* res = p->next;
        p->next = nullptr;
        return res;

    }
};
// @lc code=end

