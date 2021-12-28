#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n)
    def isBalanced(self, root: TreeNode) -> bool:
        self.is_balanced = True
        def maxDepth(root):
            if not root or not self.is_balanced:
                return -1
            l = maxDepth(root.left)
            r = maxDepth(root.right)
            if abs(l - r) > 1:
                self.is_balanced = False
                return -1
            return 1 + max(l, r)
        maxDepth(root)
        return self.is_balanced

    # # O(nlogn)
    # def isBalanced(self, root: TreeNode) -> bool:
    #     def maxDepth(root):
    #         if not root:
    #             return 0
    #         return 1 + max(maxDepth(root.left), maxDepth(root.right))
    #     if not root:
    #         return True
    #     is_balanced = abs(maxDepth(root.left) - maxDepth(root.right)) <= 1
    #     return is_balanced and self.isBalanced(root.left) and self.isBalanced(root.right)
# @lc code=end

