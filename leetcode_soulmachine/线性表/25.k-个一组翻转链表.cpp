/*
 * @lc app=leetcode.cn id=25 lang=cpp
 *
 * [25] K 个一组翻转链表
 */

// @lc code=start
/*
[1,2,3,4,5,6,7], k=3 -> [3,2,1,6,5,4,7]

// 阶段1开始状态
pdummy   ptail
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
pre      p

// 阶段1内循环结束状态
pdummy   ptail
dummy <- 1 <- 2 <- 3    4 -> 5 -> 6 -> 7
                   pre  p

// 阶段1最终状态
                   pdummy ptail
dummy -> 3 -> 2 -> 1 ->   4 -> 5 -> 6 -> 7
                 pre=None p

// 阶段1内结束状态到阶段1最终状态的转换
pdummy.next = pre
ptail.next = p
pdummy = ptail
ptail = ptail.next

*/
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        int len = 0;
        for (ListNode* node = head; node; node = node->next) {
            ++len;
        }
        int n = len / k;
        if (n == 0 || k == 1) {
            return head;
        }

        ListNode dummy = ListNode(-1);
        dummy.next = head;
        
        // keep invariant in the part cycle
        ListNode* part_dummy = &dummy;
        ListNode* part_tail = head;

        // change for every step
        ListNode* pre = nullptr;
        ListNode* p = head;
        ListNode* tmp = new ListNode(-1);

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < k; ++j) {
                tmp = p->next;
                p->next = pre;
                pre = p;
                p = tmp;
            }
            part_dummy->next = pre;
            part_tail->next = p;
            part_dummy = part_tail;
            part_tail = part_tail->next;
        }
        return dummy.next;
    }
};
// @lc code=end

