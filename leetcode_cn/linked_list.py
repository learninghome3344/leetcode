# https://leetcode-cn.com/tag/linked-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        tmp = l1.val + l2.val
        if tmp < 10:
            l3 = ListNode(tmp)
            l3.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            l3 = ListNode(tmp-10)
            carry = ListNode(1)
            l3.next = self.addTwoNumbers(self.addTwoNumbers(l1.next, carry), l2.next)
        return l3


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        p1 = head
        for _ in range(n):
            p1 = p1.next
        p = dummy
        while p1:
            p1 = p1.next
            p = p.next
        p.next = p.next.next
        return dummy.next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l3 = ListNode(l1.val)
            l3.next = self.mergeTwoLists(l1.next, l2)
        else:
            l3 = ListNode(l2.val)
            l3.next = self.mergeTwoLists(l1, l2.next)
        return l3


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))
        dummy = p = ListNode(-1)
        while heap:
            _, node = heapq.heappop(heap)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        return dummy.next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        pre, p = dummy, head
        # pre指向p的前一个节点，交换p和p.next
        while p and p.next:
            pre.next = p.next
            p.next = p.next.next
            pre.next.next = p
            pre = p
            p = p.next
        return dummy.next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head
        length = 0
        p = head
        while p:
            p = p.next
            length += 1
        loops = length // k
        dummy = ListNode(-1)
        dummy.next = head
        pre, p = dummy, head
        start, end = dummy, head
        for i in range(loops):
            for _ in range(k):
                tmp = p.next
                p.next = pre
                pre = p
                p = tmp
            start.next = pre
            end.next = p
            # start of new loop is end of last loop
            # end of new loop is start of new loop before reversed, that is p
            start, end = end, p
        return dummy.next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        cnt = 1
        p = head
        while p.next:
            p = p.next
            cnt += 1
        move = cnt - k % cnt
        p.next = head
        for _ in range(move):
            p = p.next
        res = p.next
        p.next = None
        return res


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, head
        while (cur and cur.next):
            if(cur.val == cur.next.val):
                while(cur and cur.next and cur.val == cur.next.val):
                    cur = cur.next
                pre.next = cur.next
            else:
                pre.next = cur
                pre = pre.next
            cur = cur.next
        return dummy.next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        node = head
        while node:
            while node.next and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_dummy, right_dummy = ListNode(-1), ListNode(-1)
        left_cur, right_cur = left_dummy, right_dummy
        cur = head
        while cur:
            if cur.val < x:
                left_cur.next = cur
                left_cur = cur
            else:
                right_cur.next = cur
                right_cur = cur
            cur = cur.next
        left_cur.next = right_dummy.next
        right_cur.next = None
        return left_dummy.next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next or m == n:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre, p = dummy, head
        for _ in range(m-1):
            pre = p
            p = p.next
        start, end = pre, p
        pre = None
        for _ in range(n-m+1):
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        start.next = pre
        end.next = p
        return dummy.next


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head:
            pre = None
            slow = fast = head
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            root = TreeNode(slow.val)
            if pre:
                pre.next = None
                root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(slow.next)
            return root


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        p = None
        stack = [root]
        while stack:
            node = stack.pop()
            if p:
                p.left = None
                p.right = node
            p = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        p = head
        while p:
            tmp = Node(p.val, p.next, None)
            p.next = tmp
            p = tmp.next
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        head2 = head.next
        p1, p2 = head, head2
        while p2 and p2.next:
            p1.next = p2.next
            p1 = p1.next
            p2.next = p1.next
            p2 = p2.next
        return head2


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        def getMeetingNode(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return None
        meetingNode = getMeetingNode(head)
        if not meetingNode:
            return None
        p1, p2 = meetingNode, head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p = head
        cnt = 0
        while p:
            p = p.next
            cnt += 1
        
        pre, p = None, head
        for i in range((cnt+1) // 2):
            pre = p;
            p = p.next
        pre.next = None
        right_head = p

        pre, p = None, right_head
        while p:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        right_reverse_head = pre

        left, right = head, right_reverse_head
        while right:
            tmp1, tmp2 = left.next, right.next
            left.next = right
            right.next = tmp1
            left = tmp1
            right = tmp2


class DoublyListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head, self.tail = DoublyListNode(), DoublyListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_node_to_tail(self, key):
        node = self.hashmap[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_node_to_tail(key)
        res = self.hashmap.get(key, -1)
        return res if res == -1 else res.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].val = value
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            new_node = DoublyListNode(key, value)
            self.hashmap[key] = new_node
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            new_node.prev.next = new_node
            self.tail.prev = new_node


class Solution:
    # 插入排序：每次排好一个元素，链表适合每轮找到最小值放到最左边
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur_begin = head
        while cur_begin:
            # 在cur_begin右边寻找比cur_begin小的数与之交换
            p = cur_begin.next
            while p:
                if p.val < cur_begin.val:
                    p.val, cur_begin.val = cur_begin.val, p.val
                p = p.next
            cur_begin = cur_begin.next
        return head


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 归并排序
        if not head or not head.next:
            return head
        # 找到mid
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left, right = self.sortList(head), self.sortList(mid)
        dummy = ListNode(-1)
        p = dummy
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left if left else right
        return dummy.next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1, head)
        pre, p = dummy, head
        while p:
            if p.val == val:
                pre.next = p.next
            else:
                pre = pre.next
            p = p.next
        return dummy.next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, p = None, head
        while p:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        return pre


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow表示中点
        # 1->2->3->4,slow对应3；1->2->3->4->5,slow对应3
        # 反转右边部分
        pre, cur = None, slow
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        # 现在pre是右边链表经过反转的头节点
        while head and pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd, even, even_head = head, head.next, head.next
        # 1->2->3->4->5时，even为空停止，此时形成了1->3->5->NULL和2->4->NULL
        # 1->2->3->4时，even不为空，even.next为空停止，此时形成了1->3->NULL和2->4->NULL
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


## 355 369 379

class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        import random
        res = self.head.val
        node = self.head.next
        fenmu = 2
        while node:
            if random.randint(1, fenmu) == 1:
                res = node.val
            fenmu += 1
            node = node.next
        return res


## 432

class Solution:
    # 栈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        sum_stack = []
        carry = 0
        while stack1 and stack2:
            add1, add2 = stack1.pop(), stack2.pop()
            n = add1 + add2 + carry
            if n < 10:
                sum_stack.append(n)
                carry = 0
            else:
                sum_stack.append(n-10)
                carry = 1
        if not stack1 and not stack2 and carry == 1:
            sum_stack += [1]
        else:
            stack1 = stack1 if stack1 else stack2
            while stack1:
                n = stack1.pop()
                if n+carry < 10:
                    sum_stack.append(n+carry)
                    carry = 0
                else:
                    sum_stack.append(n+carry-10)
                    carry = 1
            if carry:
                sum_stack += [1]
        dummy = ListNode(-1)
        p = dummy
        while sum_stack:
            n = sum_stack.pop()
            node = ListNode(n)
            p.next = node
            p = p.next
        return dummy.next


    # 两次反转链表
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        def reverseList(root):
            pre = None
            p = root
            while p:
                tmp = p.next
                p.next = pre
                pre = p
                p = tmp
            return pre
        l1 = reverseList(l1)
        l2 = reverseList(l2)

        def addTwoList(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            n = l1.val + l2.val
            if l1.val + l2.val < 10:
                l3 = ListNode(n)
                l3.next = addTwoList(l1.next, l2.next)
            else:
                l3 = ListNode(n-10)
                tmp = ListNode(1)
                l3.next = addTwoList(l1.next, addTwoList(l2.next, tmp))
            return l3
        res = addTwoList(l1, l2)
        res = reverseList(res)
        return res

if __name__ == '__main__':
    s = Solution()
    # s.addTwoNumbers(None, None)