# https://leetcode-cn.com/tag/linked-list/
# three parts: leetcode part, 剑指offer part, and 面试题 part
from typing import Optional, List
import collections
from unittest import result


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
leetcode part
"""

# 2.两数相加
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        cur_val = l1.val + l2.val
        if cur_val < 10:
            l3 = ListNode(cur_val)
            l3.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            l3 = ListNode(cur_val - 10)
            carry = ListNode(1)
            l3.next = self.addTwoNumbers(self.addTwoNumbers(l1.next, carry), l2.next)
        return l3
    
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        res = dummy
        carry = None
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            cval = carry.val if carry else 0
            cur_val = val1 + val2 + cval
            carry = None if cur_val < 10 else ListNode(1)
            res.next = ListNode(cur_val % 10)
            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


# 19.删除链表的倒数第N个节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast = dummy
        for _ in range(n):
            fast = fast.next
        slow = dummy
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


# 21.合并两个有序链表
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


# 23.合并k个有序链表
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
    
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        import heapq
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        
        dummy = ListNode(-1)
        p = dummy
        while heap:
            _, index = heapq.heappop(heap)
            p.next = lists[index]
            p = p.next
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
        return dummy.next


# 24.两两交换链表中的节点
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


# 25.k个一组翻转链表
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


# 61.旋转链表
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


# 82.删除排序链表中的重复元素2
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


# 83.删除排序链表中的重复元素
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


# 86.分隔链表
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


# 92.反转链表2
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


# 109.有序链表转换二叉搜索树
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


# 114.二叉树展开为链表
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


# 138. 复制带随机指针的链表
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

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


# 141.环形链表
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


# 142.环形链表2
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


# 143.重排链表
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


# 146.LRU缓存
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


# 147. 对链表进行插入排序
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


# 148.排序链表
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


# 160.相交链表
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1


# 203. 移除链表元素
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


# 206.反转链表
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, p = None, head
        while p:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        return pre


# 234.回文链表
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


# 237.删除链表中的节点
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


# 328.奇偶链表
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


# 355.设计推特
# 关注下这个pythonic的解法 
# https://leetcode-cn.com/problems/design-twitter/solution/wai-guo-wang-zhan-shang-de-gao-zan-pytho-l48z/
class Twitter:
    def __init__(self):
        self.user_followees = collections.defaultdict(set)  # user关注列表
        self.user_tweetlist = collections.defaultdict(list)  # user推文
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweetlist[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.user_followees[userId]
        top_list = self.user_tweetlist[userId][-10:]
        for followee in followees:
            top_list.extend(self.user_tweetlist[followee][-10:])
        top_list.sort(key=lambda x: x[0])
        result = [t[1] for t in top_list[-10:]][::-1]
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.user_followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_followees[followerId].discard(followeeId)


# 369.给单链表加1
# [1, 2, 3] -> [1, 2, 4]
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def reverse(head):
            pre, p = None, head
            while p:
                tmp = p.next
                p.next = pre
                pre = p
                p = tmp
            return pre
        
        head = reverse(head)
        carry = 1
        p = head
        while p:
            cur = p.val + carry
            p.val = cur % 10
            carry = cur // 10
            if carry == 0:
                break
            if not p.next and carry:
                tmp = ListNode(carry)
                p.next = tmp
                break
            p = p.next
        head = reverse(head)
        return head


# 379. 电话目录管理系统
class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.used = set()
        self.maxNumbers = maxNumbers

    def get(self) -> int:
        if len(self.used) == self.maxNumbers:
            return -1
        for n in range(self.maxNumbers):
            if n not in self.used:
                self.used.add(n)
                return n

    def check(self, number: int) -> bool:
        return number not in self.used

    def release(self, number: int) -> None:
        self.used.discard(number)


# 382.链表随机节点
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


# 426.将二叉搜索树转化为排序的双向链表
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        # 记录pre和cur，cur的left需要指向pre
        stack = []
        dummy = Node(-1)
        pre, cur = dummy, root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                pre.right = cur
                cur.left = pre
                pre = cur
                cur = cur.right
        dummy.right.left = pre
        pre.right = dummy.right
        return dummy.right


# 430. 扁平化多级双向链表
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
            if not cur.child:
                cur = cur.next
                continue
            tmp = cur.next
            child = cur.child
            cur.next = child
            cur.child = None
            child.prev = cur
            last = child
            while last.next:
                last = last.next
            last.next = tmp
            if tmp:
                tmp.prev = last
            cur = cur.next
        return head


# 432.全O(1)的数据结构


# 445.两数相加2
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































"""
剑指offer part
"""

# 剑指 Offer 06. 从尾到头打印链表
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        p = head
        stack = []
        while p:
            stack.append(p.val)
            p = p.next
        res = []
        while stack:
            res.append(stack.pop())
        return res


# 剑指 Offer 18. 删除链表的节点
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1, head)
        pre, p = dummy, head
        while p:
            if p.val == val:
                pre.next = p.next
            else:
                pre = p
            p = p.next
        return dummy.next


# 剑指 Offer 22. 链表中倒数第k个节点
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1, head)
        pre, p = dummy, dummy
        for _ in range(k):
            p = p.next
        while p:
            pre = pre.next
            p = p.next
        return pre


# 剑指 Offer 24. 反转链表
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, p = None, head
        while p:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        return pre


# 剑指 Offer 25. 合并两个排序的链表
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


# 剑指 Offer 35. 复杂链表的复制
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        # a->b  =>  a->a'->b
        p = head
        while p:
            tmp = Node(p.val, p.next)
            p.next = tmp
            p = tmp.next
        
        # every a' next
        p = head
        while p and p.next:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        
        # divide
        head_copy = head.next
        p, q = head, head_copy
        while p and p.next:
            p.next = q.next
            p = p.next
            if p:
                q.next = p.next
            q = q.next
        return head_copy


# 剑指 Offer 36. 二叉搜索树与双向链表
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':


# 剑指 Offer 52. 两个链表的第一个公共节点
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa















"""
面试题 part
"""

# 面试题 02.01. 移除重复节点












if __name__ == '__main__':
    s = Solution()
    # s.addTwoNumbers(None, None)