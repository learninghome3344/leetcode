/*
 * @lc app=leetcode.cn id=138 lang=cpp
 *
 * [138] 复制带随机指针的链表
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

/*
cout << "5: ";
Node* pp = res;
while (pp) {
    int r = -1;
    if (pp->random) {
        r = pp->random->val;
    }
    cout << pp->val << "(" << r << ")" << " -> ";
    pp = pp->next;
}
cout << endl;
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;
        Node* p = head;

        // a->b->c  =>  a->a'->b->b'->c->c'
        while (p) {
            Node* tmp = new Node(p->val);
            tmp->next = p->next;
            p->next = tmp;
            tmp->random = nullptr;
            p = tmp->next;
        }

        // update random pointer
        p = head;
        while (p) {
            if (p->random) {
                p->next->random = p->random->next;
            }
            p = p->next->next;
        }

        // divide a and a'
        p = head;
        Node* res = head->next;
        Node* q = res;
        while (q && q->next) {
            p->next = q->next;
            p = p->next;
            q->next = p->next;
            q = q->next;
        }
        p->next = nullptr;

        return res;
    }
};
// @lc code=end

