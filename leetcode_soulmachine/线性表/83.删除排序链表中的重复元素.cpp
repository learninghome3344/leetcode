/*
 * @lc app=leetcode.cn id=83 lang=cpp
 *
 * [83] 删除排序链表中的重复元素
 */

// @lc code=start
// Given 1->1->2, return 1->2.
// Given 1->1->2->3->3, return 1->2->3.
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

        if (head->val != head->next->val) {
            head->next = deleteDuplicates(head->next);
        } else {
            ListNode* tmp = head->next->next;
            delete head->next;
            head->next = tmp;
            head = deleteDuplicates(head);
        }
        return head;
    }

    /*
    // 迭代：双指针，cur一直往前走，pre指针只有在遇到新的不同的数时才往前走
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) return head;
        for (ListNode* pre = head, *cur = head->next; cur != nullptr; cur = pre->next) {
            if (pre->val == cur->val) {
                pre->next = cur->next;
                delete cur;
            } else {
                pre = cur;
            }
        }
        return head;
    }
    */

    /*
    // 迭代：保存上一个数的值，遍历链表，如果是第一次或者当前节点的值与上一个值不相等时加入结果的链表中
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) return head;
        ListNode dummy(-1);
        ListNode* cur = &dummy;
        bool is_begin = true;
        int pre_val;
        for (ListNode* node = head; node != nullptr; node = node->next) {
            if (is_begin || node->val != pre_val) {
                cur->next = node;
                cur = node;
            }
            is_begin = false;
            pre_val = node->val;
        }
        cur->next = nullptr;
        return dummy.next;
    }
    */
};
// @lc code=end

