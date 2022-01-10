/*
 * @lc app=leetcode.cn id=143 lang=cpp
 *
 * [143] 重排链表
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
    void printList(ListNode* head) {
        ListNode* p = head;
        while (p) {
            cout << p->val << " ";
            p = p->next;
        }
        cout << endl;
    }
    void reorderList(ListNode* head) {
        ListNode* p = head;
        int count = 0;
        while (p) {
            p = p->next;
            ++count;
        }

        ListNode* pre = nullptr;
        p = head;
        for (int i = 0; i < (count + 1) / 2; ++i) {
            pre = p;
            p = p->next;
        }
        pre->next = nullptr;
        ListNode* right_head = p;

        pre = nullptr;
        p = right_head;
        while (p) {
            ListNode* tmp = p->next;
            p->next = pre;
            pre = p;
            p = tmp;
        }
        ListNode* right_reverse_head = pre;

        ListNode* left = head;
        ListNode* right = right_reverse_head;
        while (right) {
            ListNode* tmp1 = left->next, *tmp2 = right->next;
            left->next = right;
            right->next = tmp1;
            left = tmp1;
            right = tmp2;
        }
    }
};
// @lc code=end

