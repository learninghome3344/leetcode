/*
 * @lc app=leetcode.cn id=92 lang=cpp
 *
 * [92] 反转链表 II
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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || !head->next || left == right) return head;

        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* pre = dummy;
        ListNode* p = head;

        for (int i = 0; i < left-1; ++i) {
            pre = p;
            p = p->next;
        }
        ListNode* part_dummy = pre;
        ListNode* part_tail = p;

        pre = nullptr;
        for (int i = 0; i < right - left + 1; ++i) {
            ListNode* tmp = p->next;
            p->next = pre;
            pre = p;
            p = tmp;
        }
        part_dummy->next = pre;
        part_tail->next = p;
        return dummy->next;
    }
};
// @lc code=end

