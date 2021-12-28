#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque([(root.left, root.right)])
        while queue:
            p, q = queue.popleft()
            if not p and not q:
                continue
            if not p or not q or (p.val != q.val):
                return False
            queue.append((p.left, q.right))
            queue.append((p.right, q.left))
        return True
    
    # # 递归方式
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     def helper(p: TreeNode, q: TreeNode) -> bool:
    #         if not p and not q:
    #             return True
    #         if not p or not q:
    #             return False
    #         return p.val == q.val and helper(p.left, q.right) and helper(p.right, q.left)
    #     if not root:
    #         return True
    #     return helper(root.left, root.right)
# @lc code=end

