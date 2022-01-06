/*
 * @lc app=leetcode.cn id=82 lang=cpp
 *
 * [82] 删除排序链表中的重复元素 II
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
    // 递归
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head || !head->next) return head;

        ListNode* p = head->next;
        if (head->val != p->val) {
            head->next = deleteDuplicates(head->next);
        } else {
            while (p && head->val == p->val) {
                ListNode* tmp = p;
                p = p->next;
                delete tmp;
            }
            delete head;
            return deleteDuplicates(p);
        }
        return head;
    }

    /*
    // 迭代：双指针
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head || !head->next) return head;

        ListNode dummy(-1);
        dummy.next = head;
        ListNode* pre = &dummy, *cur = head;
        while (cur && cur->next) {
            if (cur->val == cur->next->val) {
                while (cur && cur->next && cur->val == cur->next->val) {
                    cur = cur->next;
                }
                pre->next = cur->next;
            } else {
                pre->next = cur;
                pre = pre->next;
            }
            cur = cur->next;
        }
        return dummy.next;
    }
    */
};
// @lc code=end

