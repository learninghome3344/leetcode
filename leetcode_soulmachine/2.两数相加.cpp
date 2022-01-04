/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
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
    /*
    // 递归
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (l1 == nullptr) return l2;
        if (l2 == nullptr) return l1;
        int cur_sum = l1->val + l2->val;
        ListNode* res = new ListNode(cur_sum % 10);
        res->next = addTwoNumbers(l1->next, l2->next);
        if (cur_sum >= 10) {
            res->next = addTwoNumbers(res->next, new ListNode(1));
        }
        delete l1, l2;
        return res;
    }
    */
    
    // 迭代
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (l1 == nullptr) return l2;
        if (l2 == nullptr) return l1;

        ListNode* res = new ListNode();
        ListNode* dummy = new ListNode(0);
        res = dummy;
        int carry = 0;
        while (l1 || l2 || carry) {
            int i1 = l1 != nullptr ? l1->val : 0;
            int i2 = l2 != nullptr ? l2->val : 0;
            int cur_sum = i1 + i2 + carry;
            res->next = new ListNode(cur_sum % 10);
            res = res->next;
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
            carry = (cur_sum >= 10) ? 1: 0;
        }

        return dummy->next;
    }
};
// @lc code=end

