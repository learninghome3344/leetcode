/*
 * @lc app=leetcode.cn id=19 lang=cpp
 *
 * [19] 删除链表的倒数第 N 个结点
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
    // 双指针
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(-1);
        dummy.next = head;
        ListNode* p = &dummy, *q = &dummy;
        for (int i = 0; i < n; ++i) {
            p = p->next;
        }
        while (p->next) {
            p = p->next;
            q = q->next;
        }
        q->next = q->next->next;
        return dummy.next;
    }

    /*
    // 计算长度
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(-1);
        dummy.next = head;
        ListNode* p = &dummy;
        int len = 0;
        for (ListNode* p = head; p; p = p->next) {
            ++len;
        }
        p = &dummy;
        for (int i = 0; i < len - n; ++i) {
            p = p->next;
        }
        p->next = p->next->next;
        return dummy.next;
    }
    */
};
// @lc code=end

