/*
 * @lc app=leetcode.cn id=86 lang=cpp
 *
 * [86] 分隔链表
 */

// @lc code=start
// Given 1->4->3->2->5->2 and x = 3, return 1->2->2->4->3->5
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
    ListNode* partition(ListNode* head, int x) {
        ListNode left_dummy(-1);
        ListNode right_dummy(-1);
        ListNode* left_cur = &left_dummy;
        ListNode* right_cur = &right_dummy;

        for (ListNode* cur = head; cur != nullptr; cur = cur->next) {
            if (cur->val < x) {
                left_cur->next = cur;
                left_cur = cur;
            } else {
                right_cur->next = cur;
                right_cur = cur;
            }
        }
        left_cur->next = right_dummy.next;
        right_cur->next = nullptr;
        return left_dummy.next;
    }
};
// @lc code=end

